#!/usr/bin/env python3
"""Validate the Prompt #11 MEPL schema, example, and YAML contract.

This script validates architecture contracts only. It does not certify a workbook,
production database, connector, financial result, or public release.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "p011-mepl-manifest.schema.json"
EXAMPLE_PATH = ROOT / "examples" / "P011-MEPL-001.manifest.example.json"
CONTRACT_PATH = ROOT / "config" / "p011-mepl-001-data-model.yaml"


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = yaml.safe_load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a mapping at the top level")
    return value


def fail(message: str) -> None:
    raise AssertionError(message)


def validate_schema_and_example() -> tuple[dict[str, Any], dict[str, Any]]:
    schema = load_json(SCHEMA_PATH)
    example = load_json(EXAMPLE_PATH)

    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(example), key=lambda error: list(error.path))
    if errors:
        rendered = []
        for error in errors:
            location = ".".join(str(item) for item in error.path) or "<root>"
            rendered.append(f"- {location}: {error.message}")
        fail("Manifest example failed JSON Schema validation:\n" + "\n".join(rendered))

    return schema, example


def validate_contract(contract: dict[str, Any], example: dict[str, Any]) -> None:
    if contract.get("schema_version") != example.get("schema_version"):
        fail("YAML and example schema_version values do not match")

    module = contract.get("module", {})
    if module.get("id") != "P-011-MEPL-001":
        fail("YAML module.id must be P-011-MEPL-001")

    workbook = contract.get("workbook", {})
    sheets = workbook.get("sheets", [])
    if not isinstance(sheets, list) or not sheets:
        fail("YAML workbook.sheets must be a non-empty list")

    example_workbook = example.get("workbook", {})
    example_sheets = example_workbook.get("sheets", [])
    if example_workbook.get("sheet_count") != len(example_sheets):
        fail("Manifest workbook.sheet_count must equal the number of sheets")

    yaml_sheet_names = [sheet.get("name") for sheet in sheets]
    example_sheet_names = [sheet.get("name") for sheet in example_sheets]
    if yaml_sheet_names != example_sheet_names:
        fail("YAML and manifest workbook sheet orders do not match")

    if len(yaml_sheet_names) != len(set(yaml_sheet_names)):
        fail("Workbook sheet names must be unique")

    entities = contract.get("entities", {})
    junction_tables = contract.get("junction_tables", {})
    if not isinstance(entities, dict) or not isinstance(junction_tables, dict):
        fail("YAML entities and junction_tables must be mappings")

    declared_tables = set(entities) | set(junction_tables)
    example_required_tables = set(example.get("required_tables", []))
    missing_tables = sorted(example_required_tables - declared_tables)
    if missing_tables:
        fail("Manifest required_tables missing from YAML definitions: " + ", ".join(missing_tables))

    extra_tables = sorted(declared_tables - example_required_tables)
    if extra_tables:
        fail("YAML tables missing from manifest required_tables: " + ", ".join(extra_tables))

    id_prefixes = contract.get("id_prefixes", {})
    if not isinstance(id_prefixes, dict) or not id_prefixes:
        fail("YAML id_prefixes must be a non-empty mapping")

    for table_name, definition in entities.items():
        if not isinstance(definition, dict):
            fail(f"Entity {table_name} definition must be a mapping")
        primary_key = definition.get("primary_key")
        if not isinstance(primary_key, str) or not primary_key:
            fail(f"Entity {table_name} requires a primary_key")
        fields = definition.get("fields", [])
        if not isinstance(fields, list):
            fail(f"Entity {table_name}.fields must be a list")

    devices = entities.get("Devices", {})
    prohibited_fields = set(devices.get("prohibited_fields", []))
    required_device_prohibitions = {"password", "unlock_code", "recovery_code", "private_key"}
    if not required_device_prohibitions.issubset(prohibited_fields):
        fail("Devices must prohibit password, unlock_code, recovery_code, and private_key fields")

    model_lines = contract.get("model_lines", {})
    independent = set(model_lines.get("independent", []))
    required_independent = {
        "chatgpt_business",
        "gemini_notebooklm",
        "claude_fabric_hermes",
    }
    if independent != required_independent:
        fail("Independent model-line set does not match the Prompt #11 requirement")

    weights = contract.get("quality_score_weights", {})
    if sum(weights.values()) != 100:
        fail("quality_score_weights must sum to 100")

    release_formula = contract.get("formulas", {}).get("release_eligible", "")
    for required_term in ("Q4", "critical_gates_pass", "risk_gate!=red", "human_approval"):
        if required_term not in release_formula:
            fail(f"release_eligible formula is missing required term: {required_term}")

    public_prototype = example.get("privacy_profile", {})
    if public_prototype.get("restricted_data_included") is not False:
        fail("Public architecture example must not include restricted data")

    sample_records = example.get("sample_records", [])
    if any(record.get("synthetic_or_public") is not True for record in sample_records):
        fail("Every example sample record must be public or synthetic")

    quality = example.get("quality", {})
    if quality.get("human_approval_status") == "approved":
        fail("Architecture example must not claim human approval")
    if quality.get("decision") in {"q3_approved", "q4_approved"}:
        fail("Architecture example must not claim Q3 or Q4 approval before implementation")

    stop_work = set(contract.get("stop_work", []))
    required_stop_conditions = {
        "restricted_data_in_public_prototype",
        "model_line_copy_mislabeled_as_independent",
        "human_approval_set_by_ai",
        "workbook_corruption_or_untraceable_dashboard_metric",
    }
    if not required_stop_conditions.issubset(stop_work):
        missing = sorted(required_stop_conditions - stop_work)
        fail("Missing required stop-work conditions: " + ", ".join(missing))


def main() -> int:
    try:
        _, example = validate_schema_and_example()
        contract = load_yaml(CONTRACT_PATH)
        validate_contract(contract, example)
    except (OSError, ValueError, json.JSONDecodeError, yaml.YAMLError, AssertionError) as exc:
        print(f"MEPL contract validation FAILED: {exc}", file=sys.stderr)
        return 1

    print("MEPL contract validation PASSED")
    print(f"- JSON Schema: {SCHEMA_PATH.relative_to(ROOT)}")
    print(f"- Manifest example: {EXAMPLE_PATH.relative_to(ROOT)}")
    print(f"- YAML contract: {CONTRACT_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
