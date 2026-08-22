#!/usr/bin/env python3
"""Prompt #11 XPIO Q2 control-plane prototype.

Standard-library only. This prototype provides a portable SQLite registry for
Prompt #11 artifacts, aliases, platforms, identity passports, work packets,
transparency events, defects, decisions, diagnostics, and documents.

It does not connect to external platforms, store secrets, execute payments,
impersonate a person, deploy mutations, or pass HumanApprovalGate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import sys
import uuid
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

SCHEMA_VERSION = 1
PRIVACY_RANK = {"public": 0, "internal": 1, "confidential": 2, "restricted": 3}
Q_RANK = {f"Q{i}": i for i in range(8)}

DEFAULT_PLATFORMS = [
    {
        "platform_id": "PLAT-CHATGPT",
        "name": "ChatGPT Business",
        "role": "orchestration_and_chatgpt_model_line",
        "operational_claim": "connected_conversation_only",
        "max_privacy_class": "confidential",
        "status": "partially_verified",
        "revocation_method": "Remove workspace access and revoke related credentials.",
    },
    {
        "platform_id": "PLAT-GITHUB",
        "name": "GitHub",
        "role": "canonical_source_control",
        "operational_claim": "connected",
        "max_privacy_class": "internal",
        "status": "verified",
        "revocation_method": "Revoke app or token permissions and repository access.",
    },
    {
        "platform_id": "PLAT-SLACK",
        "name": "Slack",
        "role": "coordination_and_notifications",
        "operational_claim": "connected_private_channel",
        "max_privacy_class": "internal",
        "status": "verified",
        "revocation_method": "Remove app, member, or channel permissions.",
    },
    {
        "platform_id": "PLAT-GEMINI",
        "name": "Gemini",
        "role": "independent_research_line",
        "operational_claim": "handoff_contract_only",
        "max_privacy_class": "public",
        "status": "not_tested",
        "revocation_method": "Remove account or notebook permissions and delete copied data.",
    },
    {
        "platform_id": "PLAT-NOTEBOOKLM",
        "name": "NotebookLM",
        "role": "source_grounded_notebooks",
        "operational_claim": "handoff_contract_only",
        "max_privacy_class": "public",
        "status": "not_tested",
        "revocation_method": "Remove notebook sources and sharing permissions.",
    },
    {
        "platform_id": "PLAT-CLAUDE",
        "name": "Claude",
        "role": "independent_review_line",
        "operational_claim": "handoff_contract_only",
        "max_privacy_class": "public",
        "status": "not_tested",
        "revocation_method": "Remove project access and copied data.",
    },
    {
        "platform_id": "PLAT-HERMES",
        "name": "Fabric Hermes",
        "role": "dispatch_audit_and_quality",
        "operational_claim": "architecture_and_repository_mirror",
        "max_privacy_class": "internal",
        "status": "architecture_only",
        "revocation_method": "Suspend agent passport and connector permissions.",
    },
    {
        "platform_id": "PLAT-ZO",
        "name": "lippytmai.zo.computer",
        "role": "bounded_runtime_experiments",
        "operational_claim": "runtime_contract_only",
        "max_privacy_class": "public",
        "status": "not_tested",
        "revocation_method": "Stop runtime, revoke secrets, and delete experiment data.",
    },
    {
        "platform_id": "PLAT-MEPL",
        "name": "Master Evidence and Product Ledger",
        "role": "evidence_and_product_ledger",
        "operational_claim": "q3_workbook_artifact",
        "max_privacy_class": "internal",
        "status": "q3_artifact",
        "revocation_method": "Withdraw workbook access and issue a superseding version.",
    },
]

MANDATORY_CLONE_PROHIBITION_TERMS = (
    "impersonate",
    "fabricate personal memories",
    "move money",
    "sign contracts",
    "expand permissions",
    "humanapprovalgate",
    "deploy its own mutations",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def stable_id(prefix: str, value: str, length: int = 16) -> str:
    digest = hashlib.sha256(value.encode("utf-8")).hexdigest()[:length].upper()
    return f"{prefix}-{digest}"


def json_text(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(",", ":"))


def parse_json(text: str | None, default: Any) -> Any:
    if not text:
        return default
    return json.loads(text)


def privacy_route_allowed(data_class: str, platform_max: str) -> bool:
    if data_class not in PRIVACY_RANK or platform_max not in PRIVACY_RANK:
        return False
    return PRIVACY_RANK[data_class] <= PRIVACY_RANK[platform_max]


def release_eligible(
    q_stage: str,
    risk_gate: str,
    critical_gates_passed: bool,
    human_approval_status: str,
    approver_type: str = "human",
) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    if Q_RANK.get(q_stage, -1) < Q_RANK["Q4"]:
        reasons.append("minimum Q4 certification not met")
    if risk_gate == "Red":
        reasons.append("Red RiskGate blocks release")
    if not critical_gates_passed:
        reasons.append("one or more critical gates failed or remain untested")
    if human_approval_status != "approved":
        reasons.append("HumanApprovalGate is not approved")
    if approver_type != "human":
        reasons.append("HumanApprovalGate approver is not a human")
    return (not reasons, reasons)


@dataclass(frozen=True)
class DiagnosticResult:
    check_name: str
    status: str
    severity: str
    object_type: str
    object_id: str
    summary: str
    evidence: str

    @property
    def diag_id(self) -> str:
        seed = f"{self.check_name}|{self.object_type}|{self.object_id}|{self.summary}"
        return stable_id("DIAG-XPIO", seed, 20)


class XPIOControlPlane:
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(db_path))
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.conn.execute("PRAGMA journal_mode = WAL")

    def close(self) -> None:
        self.conn.close()

    def __enter__(self) -> "XPIOControlPlane":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        if exc:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.close()

    def initialize(self) -> None:
        schema = """
        CREATE TABLE IF NOT EXISTS migrations (
            version INTEGER PRIMARY KEY,
            applied_at TEXT NOT NULL,
            description TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS artifacts (
            artifact_id TEXT PRIMARY KEY,
            canonical_name TEXT NOT NULL,
            sha256 TEXT NOT NULL UNIQUE,
            size_bytes INTEGER NOT NULL CHECK(size_bytes >= 0),
            extension TEXT,
            category TEXT NOT NULL,
            privacy_class TEXT NOT NULL,
            status TEXT NOT NULL,
            source_path TEXT,
            registered_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS artifact_aliases (
            alias_name TEXT PRIMARY KEY,
            artifact_id TEXT NOT NULL REFERENCES artifacts(artifact_id),
            original_path TEXT,
            duplicate_content INTEGER NOT NULL CHECK(duplicate_content IN (0,1))
        );
        CREATE TABLE IF NOT EXISTS platforms (
            platform_id TEXT PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            role TEXT NOT NULL,
            operational_claim TEXT NOT NULL,
            max_privacy_class TEXT NOT NULL,
            status TEXT NOT NULL,
            revocation_method TEXT NOT NULL,
            last_verified_at TEXT
        );
        CREATE TABLE IF NOT EXISTS identities (
            identity_id TEXT PRIMARY KEY,
            identity_type TEXT NOT NULL,
            display_name TEXT NOT NULL,
            human_owner TEXT NOT NULL,
            disclosure TEXT NOT NULL,
            permitted_roles_json TEXT NOT NULL,
            permitted_memory_classes_json TEXT NOT NULL,
            prohibited_actions_json TEXT NOT NULL,
            platform_scope_json TEXT NOT NULL,
            status TEXT NOT NULL,
            human_approver TEXT NOT NULL,
            version TEXT,
            revoked_at TEXT
        );
        CREATE TABLE IF NOT EXISTS work_packets (
            work_packet_id TEXT PRIMARY KEY,
            correlation_id TEXT NOT NULL,
            title TEXT NOT NULL,
            objective TEXT NOT NULL,
            human_owner TEXT NOT NULL,
            source_platform TEXT NOT NULL,
            model_line TEXT NOT NULL,
            privacy_class TEXT NOT NULL,
            status TEXT NOT NULL,
            human_approval_status TEXT NOT NULL,
            q_stage TEXT NOT NULL DEFAULT 'Q2',
            risk_gate TEXT NOT NULL DEFAULT 'Yellow',
            critical_gates_passed INTEGER NOT NULL DEFAULT 0 CHECK(critical_gates_passed IN (0,1)),
            next_action TEXT,
            payload_json TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS documents (
            document_id TEXT PRIMARY KEY,
            document_class TEXT NOT NULL,
            title TEXT NOT NULL,
            version TEXT NOT NULL,
            path TEXT NOT NULL,
            sha256 TEXT NOT NULL,
            status TEXT NOT NULL,
            owner TEXT NOT NULL,
            review_due_at TEXT,
            supersedes_document_id TEXT
        );
        CREATE TABLE IF NOT EXISTS events (
            event_id TEXT PRIMARY KEY,
            correlation_id TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            actor_type TEXT NOT NULL,
            actor_id TEXT NOT NULL,
            platform_id TEXT,
            model_line TEXT,
            event_type TEXT NOT NULL,
            object_type TEXT NOT NULL,
            object_id TEXT NOT NULL,
            severity TEXT NOT NULL,
            result TEXT NOT NULL,
            summary TEXT NOT NULL,
            rationale_summary TEXT,
            evidence_reference TEXT,
            details_json TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS defects (
            defect_id TEXT PRIMARY KEY,
            correlation_id TEXT NOT NULL,
            title TEXT NOT NULL,
            severity TEXT NOT NULL,
            status TEXT NOT NULL,
            expected_behavior TEXT NOT NULL,
            actual_behavior TEXT NOT NULL,
            reproduction_steps TEXT NOT NULL,
            root_cause TEXT,
            fix_reference TEXT,
            regression_test_reference TEXT,
            release_blocking INTEGER NOT NULL CHECK(release_blocking IN (0,1)),
            created_at TEXT NOT NULL,
            closed_at TEXT
        );
        CREATE TABLE IF NOT EXISTS decisions (
            decision_id TEXT PRIMARY KEY,
            object_type TEXT NOT NULL,
            object_id TEXT NOT NULL,
            decision TEXT NOT NULL,
            rationale_summary TEXT NOT NULL,
            approver_type TEXT NOT NULL,
            approver_id TEXT NOT NULL,
            decided_at TEXT NOT NULL,
            status TEXT NOT NULL,
            supersedes_decision_id TEXT
        );
        CREATE TABLE IF NOT EXISTS diagnostics (
            diag_id TEXT PRIMARY KEY,
            check_name TEXT NOT NULL,
            status TEXT NOT NULL,
            severity TEXT NOT NULL,
            object_type TEXT NOT NULL,
            object_id TEXT NOT NULL,
            summary TEXT NOT NULL,
            evidence TEXT NOT NULL,
            timestamp TEXT NOT NULL
        );
        """
        with self.conn:
            self.conn.executescript(schema)
            self.conn.execute(
                "INSERT OR IGNORE INTO migrations(version, applied_at, description) VALUES (?, ?, ?)",
                (SCHEMA_VERSION, utc_now(), "Initial XPIO Q2 schema"),
            )

    def register_default_platforms(self) -> None:
        with self.conn:
            for p in DEFAULT_PLATFORMS:
                self.conn.execute(
                    """
                    INSERT INTO platforms(platform_id,name,role,operational_claim,max_privacy_class,status,revocation_method,last_verified_at)
                    VALUES(:platform_id,:name,:role,:operational_claim,:max_privacy_class,:status,:revocation_method,:last_verified_at)
                    ON CONFLICT(platform_id) DO UPDATE SET
                      name=excluded.name,
                      role=excluded.role,
                      operational_claim=excluded.operational_claim,
                      max_privacy_class=excluded.max_privacy_class,
                      status=excluded.status,
                      revocation_method=excluded.revocation_method,
                      last_verified_at=excluded.last_verified_at
                    """,
                    {**p, "last_verified_at": utc_now() if p["status"] == "verified" else None},
                )

    def import_artifact_manifest(self, manifest_path: Path) -> tuple[int, int]:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        aliases = manifest.get("artifacts", manifest.get("artifact_aliases", []))
        unique_by_id: dict[str, dict[str, Any]] = {}
        for r in aliases:
            unique_by_id.setdefault(r["artifact_id"], r)
            if not r.get("duplicate_content"):
                unique_by_id[r["artifact_id"]] = r
        with self.conn:
            for aid, r in unique_by_id.items():
                source_path = r.get("original_path")
                self.conn.execute(
                    """
                    INSERT INTO artifacts(artifact_id,canonical_name,sha256,size_bytes,extension,category,privacy_class,status,source_path,registered_at)
                    VALUES(?,?,?,?,?,?,?,?,?,?)
                    ON CONFLICT(artifact_id) DO UPDATE SET
                      canonical_name=excluded.canonical_name,
                      sha256=excluded.sha256,
                      size_bytes=excluded.size_bytes,
                      extension=excluded.extension,
                      category=excluded.category,
                      privacy_class=excluded.privacy_class,
                      status=excluded.status,
                      source_path=excluded.source_path,
                      registered_at=excluded.registered_at
                    """,
                    (
                        aid, r["canonical_name"], r["sha256"], int(r["size_bytes"]), r.get("extension"),
                        r["category"], r["privacy_class"], r["status"], source_path, r["registered_at"],
                    ),
                )
            for r in aliases:
                self.conn.execute(
                    """
                    INSERT INTO artifact_aliases(alias_name,artifact_id,original_path,duplicate_content)
                    VALUES(?,?,?,?)
                    ON CONFLICT(alias_name) DO UPDATE SET
                      artifact_id=excluded.artifact_id,
                      original_path=excluded.original_path,
                      duplicate_content=excluded.duplicate_content
                    """,
                    (r["alias_name"], r["artifact_id"], r.get("original_path"), int(bool(r.get("duplicate_content")))),
                )
        return len(unique_by_id), len(aliases)

    def import_identity_passport(self, path: Path) -> str:
        p = json.loads(path.read_text(encoding="utf-8"))
        with self.conn:
            self.conn.execute(
                """
                INSERT INTO identities(identity_id,identity_type,display_name,human_owner,disclosure,permitted_roles_json,
                  permitted_memory_classes_json,prohibited_actions_json,platform_scope_json,status,human_approver,version,revoked_at)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,NULL)
                ON CONFLICT(identity_id) DO UPDATE SET
                  identity_type=excluded.identity_type, display_name=excluded.display_name,
                  human_owner=excluded.human_owner, disclosure=excluded.disclosure,
                  permitted_roles_json=excluded.permitted_roles_json,
                  permitted_memory_classes_json=excluded.permitted_memory_classes_json,
                  prohibited_actions_json=excluded.prohibited_actions_json,
                  platform_scope_json=excluded.platform_scope_json,
                  status=excluded.status, human_approver=excluded.human_approver, version=excluded.version
                """,
                (
                    p["identity_id"], p["identity_type"], p["display_name"], p["human_owner"], p["disclosure"],
                    json_text(p.get("permitted_roles", [])), json_text(p.get("permitted_memory_classes", [])),
                    json_text(p.get("prohibited_actions", [])), json_text(p.get("platform_scope", [])),
                    p["status"], p["human_approver"], p.get("version"),
                ),
            )
        return p["identity_id"]

    def import_work_packet(self, path: Path) -> str:
        p = json.loads(path.read_text(encoding="utf-8"))
        with self.conn:
            self.conn.execute(
                """
                INSERT INTO work_packets(work_packet_id,correlation_id,title,objective,human_owner,source_platform,model_line,
                  privacy_class,status,human_approval_status,q_stage,risk_gate,critical_gates_passed,next_action,payload_json,created_at,updated_at)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                ON CONFLICT(work_packet_id) DO UPDATE SET
                  correlation_id=excluded.correlation_id, title=excluded.title, objective=excluded.objective,
                  human_owner=excluded.human_owner, source_platform=excluded.source_platform,
                  model_line=excluded.model_line, privacy_class=excluded.privacy_class, status=excluded.status,
                  human_approval_status=excluded.human_approval_status, q_stage=excluded.q_stage,
                  risk_gate=excluded.risk_gate, critical_gates_passed=excluded.critical_gates_passed,
                  next_action=excluded.next_action, payload_json=excluded.payload_json, updated_at=excluded.updated_at
                """,
                (
                    p["work_packet_id"], p["correlation_id"], p["title"], p["objective"], p["human_owner"],
                    p["source_platform"], p["model_line"], p["privacy_class"], p["status"],
                    p["human_approval_status"], p.get("q_stage", "Q2"), p.get("risk_gate", "Yellow"),
                    int(bool(p.get("critical_gates_passed", False))), p.get("next_action"), json_text(p),
                    p.get("created_at", utc_now()), p.get("updated_at", utc_now()),
                ),
            )
        return p["work_packet_id"]

    def register_document(self, path: Path, document_class: str, owner: str = "Charles Earl Lipshay") -> str:
        doc_id = stable_id("DOC-XPIO", str(path.resolve()), 20)
        digest = sha256_file(path)
        with self.conn:
            self.conn.execute(
                """
                INSERT INTO documents(document_id,document_class,title,version,path,sha256,status,owner,review_due_at,supersedes_document_id)
                VALUES(?,?,?,?,?,?,?,?,NULL,NULL)
                ON CONFLICT(document_id) DO UPDATE SET
                  document_class=excluded.document_class, title=excluded.title, version=excluded.version,
                  path=excluded.path, sha256=excluded.sha256, status=excluded.status, owner=excluded.owner
                """,
                (doc_id, document_class, path.stem, "0.1", str(path), digest, "review_ready", owner),
            )
        return doc_id

    def record_event(
        self, *, correlation_id: str, actor_type: str, actor_id: str, event_type: str,
        object_type: str, object_id: str, severity: str, result: str, summary: str,
        platform_id: str | None = None, model_line: str | None = None,
        rationale_summary: str | None = None, evidence_reference: str | None = None,
        details: dict[str, Any] | None = None,
    ) -> str:
        if not correlation_id or len(correlation_id) < 8:
            raise ValueError("correlation_id must contain at least 8 characters")
        event_id = stable_id("EVT-XPIO", f"{correlation_id}|{event_type}|{object_type}|{object_id}|{utc_now()}|{uuid.uuid4()}", 24)
        with self.conn:
            self.conn.execute(
                """
                INSERT INTO events(event_id,correlation_id,timestamp,actor_type,actor_id,platform_id,model_line,event_type,
                  object_type,object_id,severity,result,summary,rationale_summary,evidence_reference,details_json)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    event_id, correlation_id, utc_now(), actor_type, actor_id, platform_id, model_line, event_type,
                    object_type, object_id, severity, result, summary, rationale_summary, evidence_reference,
                    json_text(details or {}),
                ),
            )
        return event_id

    def add_decision(
        self, *, object_type: str, object_id: str, decision: str, rationale_summary: str,
        approver_type: str, approver_id: str, status: str,
    ) -> str:
        if decision.lower().startswith("humanapproval") and approver_type != "human":
            raise ValueError("HumanApprovalGate may be decided only by a human approver")
        did = stable_id("DEC-XPIO", f"{object_type}|{object_id}|{decision}|{utc_now()}|{uuid.uuid4()}", 20)
        with self.conn:
            self.conn.execute(
                """
                INSERT INTO decisions(decision_id,object_type,object_id,decision,rationale_summary,approver_type,approver_id,decided_at,status,supersedes_decision_id)
                VALUES(?,?,?,?,?,?,?,?,?,NULL)
                """,
                (did, object_type, object_id, decision, rationale_summary, approver_type, approver_id, utc_now(), status),
            )
        return did

    def verify_artifacts(self) -> list[DiagnosticResult]:
        results: list[DiagnosticResult] = []
        for row in self.conn.execute("SELECT * FROM artifacts ORDER BY artifact_id"):
            p = Path(row["source_path"]) if row["source_path"] else None
            if not p or not p.exists():
                results.append(DiagnosticResult(
                    "artifact_hash_integrity", "WARN", "WARN", "artifact", row["artifact_id"],
                    f"Local source path is unavailable for {row['canonical_name']}", str(p) if p else "no path",
                ))
                continue
            actual_size = p.stat().st_size
            actual_hash = sha256_file(p)
            if actual_hash != row["sha256"] or actual_size != row["size_bytes"]:
                results.append(DiagnosticResult(
                    "artifact_hash_integrity", "FAIL", "CRITICAL", "artifact", row["artifact_id"],
                    f"Hash or size mismatch for {row['canonical_name']}",
                    f"expected_sha={row['sha256']} actual_sha={actual_hash} expected_size={row['size_bytes']} actual_size={actual_size}",
                ))
            else:
                results.append(DiagnosticResult(
                    "artifact_hash_integrity", "PASS", "INFO", "artifact", row["artifact_id"],
                    f"Verified {row['canonical_name']}", actual_hash,
                ))
        return results

    def run_diagnostics(self) -> list[DiagnosticResult]:
        results: list[DiagnosticResult] = []
        integrity = self.conn.execute("PRAGMA integrity_check").fetchone()[0]
        results.append(DiagnosticResult(
            "database_integrity", "PASS" if integrity == "ok" else "FAIL",
            "INFO" if integrity == "ok" else "CRITICAL", "database", str(self.db_path),
            "SQLite integrity check completed", integrity,
        ))
        migration = self.conn.execute("SELECT MAX(version) FROM migrations").fetchone()[0]
        results.append(DiagnosticResult(
            "database_migration", "PASS" if migration == SCHEMA_VERSION else "FAIL",
            "INFO" if migration == SCHEMA_VERSION else "ERROR", "database", str(self.db_path),
            f"Schema version is {migration}", f"required={SCHEMA_VERSION}",
        ))
        artifact_count = self.conn.execute("SELECT COUNT(*) FROM artifacts").fetchone()[0]
        alias_count = self.conn.execute("SELECT COUNT(*) FROM artifact_aliases").fetchone()[0]
        duplicate_count = self.conn.execute("SELECT COUNT(*) FROM artifact_aliases WHERE duplicate_content=1").fetchone()[0]
        results.append(DiagnosticResult(
            "artifact_registry_coverage", "PASS" if artifact_count > 0 and alias_count >= artifact_count else "FAIL",
            "INFO" if artifact_count > 0 and alias_count >= artifact_count else "ERROR", "vault", "P011-ARTIFACT-VAULT-001",
            f"Registered {artifact_count} unique artifacts and {alias_count} aliases", f"duplicate_aliases={duplicate_count}",
        ))
        results.extend(self.verify_artifacts())
        for p in self.conn.execute("SELECT * FROM platforms ORDER BY platform_id"):
            status = "PASS" if p["status"] == "verified" else "WARN"
            results.append(DiagnosticResult(
                "platform_operational_claim", status, "INFO" if status == "PASS" else "WARN", "platform", p["platform_id"],
                f"{p['name']} status is {p['status']}", p["operational_claim"],
            ))
            if not p["revocation_method"].strip():
                results.append(DiagnosticResult(
                    "platform_revocation", "FAIL", "CRITICAL", "platform", p["platform_id"],
                    "Revocation method is missing", "",
                ))
        for i in self.conn.execute("SELECT * FROM identities ORDER BY identity_id"):
            prohibited = [str(x).lower() for x in parse_json(i["prohibited_actions_json"], [])]
            joined = " | ".join(prohibited)
            missing = [t for t in MANDATORY_CLONE_PROHIBITION_TERMS if t not in joined]
            status = "PASS" if not missing else "FAIL"
            results.append(DiagnosticResult(
                "clone_identity_boundary", status, "INFO" if status == "PASS" else "CRITICAL", "identity", i["identity_id"],
                "Clone identity boundaries are complete" if not missing else "Clone identity boundaries are incomplete",
                "missing=" + ",".join(missing),
            ))
            if i["human_approver"].upper().startswith(("CLONE-", "AGENT-", "SWARM-")):
                results.append(DiagnosticResult(
                    "human_approval_identity", "FAIL", "CRITICAL", "identity", i["identity_id"],
                    "Human approver is not a human identity", i["human_approver"],
                ))
        platform_by_name = {r["name"].lower(): r for r in self.conn.execute("SELECT * FROM platforms")}
        for wp in self.conn.execute("SELECT * FROM work_packets ORDER BY work_packet_id"):
            platform = platform_by_name.get(wp["source_platform"].lower())
            if platform and not privacy_route_allowed(wp["privacy_class"], platform["max_privacy_class"]):
                results.append(DiagnosticResult(
                    "privacy_route", "FAIL", "CRITICAL", "work_packet", wp["work_packet_id"],
                    f"{wp['privacy_class']} data exceeds {platform['name']} route allowance", f"platform_max={platform['max_privacy_class']}",
                ))
            eligible, reasons = release_eligible(
                wp["q_stage"], wp["risk_gate"], bool(wp["critical_gates_passed"]), wp["human_approval_status"], "human"
            )
            if wp["status"] == "released" and not eligible:
                results.append(DiagnosticResult(
                    "release_boundary", "FAIL", "CRITICAL", "work_packet", wp["work_packet_id"],
                    "Work packet is marked released but release requirements are not met", "; ".join(reasons),
                ))
            else:
                results.append(DiagnosticResult(
                    "release_boundary", "PASS" if eligible else "WARN", "INFO" if eligible else "WARN", "work_packet", wp["work_packet_id"],
                    "Release requirements met" if eligible else "Release remains blocked or review-only", "; ".join(reasons),
                ))
        doc_classes = {r[0] for r in self.conn.execute("SELECT DISTINCT document_class FROM documents")}
        required_docs = {"canonical_architecture", "diagnostics_manual", "database_transparency", "identity_strategy", "artifact_vault"}
        missing_docs = sorted(required_docs - doc_classes)
        results.append(DiagnosticResult(
            "documentation_coverage", "PASS" if not missing_docs else "FAIL",
            "INFO" if not missing_docs else "ERROR", "module", "P-011-XPIO-001",
            "Required document classes are registered" if not missing_docs else "Required document classes are missing",
            "missing=" + ",".join(missing_docs),
        ))
        event_count = self.conn.execute("SELECT COUNT(*) FROM events").fetchone()[0]
        missing_corr = self.conn.execute("SELECT COUNT(*) FROM events WHERE correlation_id IS NULL OR length(correlation_id)<8").fetchone()[0]
        results.append(DiagnosticResult(
            "transparency_event_integrity", "PASS" if event_count > 0 and missing_corr == 0 else "WARN",
            "INFO" if event_count > 0 and missing_corr == 0 else "WARN", "event_log", "XPIO-EVENTS",
            f"Transparency log contains {event_count} events", f"invalid_correlation_ids={missing_corr}",
        ))
        backup_success = self.conn.execute(
            "SELECT COUNT(*) FROM events WHERE event_type='backup_restore_test' AND result='SUCCESS'"
        ).fetchone()[0]
        results.append(DiagnosticResult(
            "backup_restore_evidence", "PASS" if backup_success else "NOT_TESTED",
            "INFO" if backup_success else "WARN", "database", str(self.db_path),
            "Backup and restore test evidence is present" if backup_success else "Backup and restore must be tested before Q3",
            f"successful_tests={backup_success}" if backup_success else "No restore test record in Q2 prototype",
        ))
        results.append(DiagnosticResult(
            "model_line_independence", "NOT_TESTED", "WARN", "module", "P-011-XPIO-001",
            "Independent Gemini/NotebookLM and Claude/Hermes reviews remain pending", "Q3 dependency",
        ))
        return results

    def store_diagnostics(self, results: Iterable[DiagnosticResult]) -> None:
        with self.conn:
            for r in results:
                self.conn.execute(
                    """
                    INSERT INTO diagnostics(diag_id,check_name,status,severity,object_type,object_id,summary,evidence,timestamp)
                    VALUES(?,?,?,?,?,?,?,?,?)
                    ON CONFLICT(diag_id) DO UPDATE SET
                      status=excluded.status, severity=excluded.severity, summary=excluded.summary,
                      evidence=excluded.evidence, timestamp=excluded.timestamp
                    """,
                    (r.diag_id, r.check_name, r.status, r.severity, r.object_type, r.object_id, r.summary, r.evidence, utc_now()),
                )

    def report_data(self) -> dict[str, Any]:
        diagnostics = [dict(r) for r in self.conn.execute("SELECT * FROM diagnostics ORDER BY severity DESC, check_name, object_id")]
        counts = {
            "artifacts": self.conn.execute("SELECT COUNT(*) FROM artifacts").fetchone()[0],
            "aliases": self.conn.execute("SELECT COUNT(*) FROM artifact_aliases").fetchone()[0],
            "platforms": self.conn.execute("SELECT COUNT(*) FROM platforms").fetchone()[0],
            "identities": self.conn.execute("SELECT COUNT(*) FROM identities").fetchone()[0],
            "work_packets": self.conn.execute("SELECT COUNT(*) FROM work_packets").fetchone()[0],
            "documents": self.conn.execute("SELECT COUNT(*) FROM documents").fetchone()[0],
            "events": self.conn.execute("SELECT COUNT(*) FROM events").fetchone()[0],
            "defects": self.conn.execute("SELECT COUNT(*) FROM defects").fetchone()[0],
            "decisions": self.conn.execute("SELECT COUNT(*) FROM decisions").fetchone()[0],
            "diagnostics": len(diagnostics),
        }
        summary = {s: sum(1 for d in diagnostics if d["status"] == s) for s in ["PASS", "WARN", "FAIL", "NOT_TESTED"]}
        return {
            "module_id": "P-011-XPIO-001", "generated_at": utc_now(), "database": str(self.db_path),
            "q_stage": "Q2", "risk_gate": "Yellow", "human_approval_gate": "pending",
            "counts": counts, "diagnostic_summary": summary, "diagnostics": diagnostics,
            "platforms": [dict(r) for r in self.conn.execute("SELECT * FROM platforms ORDER BY platform_id")],
            "identities": [dict(r) for r in self.conn.execute("SELECT identity_id,identity_type,display_name,human_owner,status,human_approver,version FROM identities ORDER BY identity_id")],
            "work_packets": [dict(r) for r in self.conn.execute("SELECT work_packet_id,correlation_id,title,status,q_stage,risk_gate,human_approval_status,next_action FROM work_packets ORDER BY work_packet_id")],
            "release_boundary": {
                "q3_approved": False, "q4_inventory_approved": False, "production_deployment_approved": False,
                "financial_action_approved": False, "autonomous_mutation_approved": False,
            },
        }

    def write_reports(self, json_path: Path, markdown_path: Path) -> None:
        data = self.report_data()
        json_path.parent.mkdir(parents=True, exist_ok=True)
        markdown_path.parent.mkdir(parents=True, exist_ok=True)
        json_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        s = data["diagnostic_summary"]
        lines = [
            "# P-011-XPIO-001 Q2 Transparency and Diagnostics Report", "", f"Generated: {data['generated_at']}", "",
            "## Decision", "", "- Q stage: Q2 Structured Implementation", "- RiskGate: Yellow",
            "- HumanApprovalGate: pending", "- Q3 and Q4: not approved",
            "- Production deployment, financial action, autonomous mutation, public release, NFT minting, and franchise replication: not approved",
            "", "## Registry counts", "",
        ]
        for k, v in data["counts"].items():
            lines.append(f"- {k}: {v}")
        lines += [
            "", "## Diagnostic summary", "", f"- PASS: {s.get('PASS',0)}", f"- WARN: {s.get('WARN',0)}",
            f"- FAIL: {s.get('FAIL',0)}", f"- NOT_TESTED: {s.get('NOT_TESTED',0)}", "", "## Findings", "",
            "| Check | Status | Severity | Object | Summary | Evidence |", "|---|---|---|---|---|---|",
        ]
        for d in data["diagnostics"]:
            clean = lambda x: str(x).replace("|", "/").replace("\n", " ")
            lines.append(f"| {clean(d['check_name'])} | {clean(d['status'])} | {clean(d['severity'])} | {clean(d['object_id'])} | {clean(d['summary'])} | {clean(d['evidence'])} |")
        lines += [
            "", "## Transparency boundary", "",
            "This report records evidence, tests, states, and concise rationale summaries. It does not expose private chain-of-thought, secrets, or restricted personal records.",
        ]
        markdown_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def bootstrap(args: argparse.Namespace) -> int:
    db = Path(args.db)
    with XPIOControlPlane(db) as cp:
        cp.initialize()
        cp.register_default_platforms()
        unique, aliases = cp.import_artifact_manifest(Path(args.manifest))
        identity_id = cp.import_identity_passport(Path(args.identity))
        work_packet_id = cp.import_work_packet(Path(args.work_packet))
        for spec in args.document:
            document_class, path = spec.split("=", 1)
            cp.register_document(Path(path), document_class)
        cp.record_event(
            correlation_id="CORR-XPIO-20260822-BOOTSTRAP", actor_type="system", actor_id="XPIO-Q2-PROTOTYPE",
            platform_id="PLAT-GITHUB", model_line="chatgpt", event_type="bootstrap_completed", object_type="module",
            object_id="P-011-XPIO-001", severity="INFO", result="SUCCESS",
            summary=f"Imported {unique} unique artifacts and {aliases} aliases", evidence_reference=str(Path(args.manifest)),
            details={"identity_id": identity_id, "work_packet_id": work_packet_id},
        )
        results = cp.run_diagnostics()
        cp.store_diagnostics(results)
        cp.write_reports(Path(args.json_report), Path(args.markdown_report))
        fail_count = sum(1 for r in results if r.status == "FAIL")
        print(json.dumps({
            "database": str(db), "unique_artifacts": unique, "aliases": aliases, "diagnostics": len(results),
            "failures": fail_count, "json_report": args.json_report, "markdown_report": args.markdown_report,
        }, indent=2))
        return 1 if fail_count else 0


def command_diagnose(args: argparse.Namespace) -> int:
    with XPIOControlPlane(Path(args.db)) as cp:
        cp.initialize()
        results = cp.run_diagnostics()
        cp.store_diagnostics(results)
        cp.write_reports(Path(args.json_report), Path(args.markdown_report))
        failures = [asdict(r) for r in results if r.status == "FAIL"]
        print(json.dumps({"results": len(results), "failures": failures}, indent=2))
        return 1 if failures else 0


def command_backup_test(args: argparse.Namespace) -> int:
    db_path = Path(args.db)
    backup_path = Path(args.backup)
    report_path = Path(args.report)
    backup_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with XPIOControlPlane(db_path) as cp:
        cp.initialize()
        target = sqlite3.connect(str(backup_path))
        try:
            cp.conn.backup(target)
            target.commit()
            integrity = target.execute("PRAGMA integrity_check").fetchone()[0]
            source_counts = {
                table: cp.conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
                for table in ("artifacts", "artifact_aliases", "platforms", "identities", "work_packets", "documents", "events")
            }
            backup_counts = {
                table: target.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
                for table in source_counts
            }
            counts_match = source_counts == backup_counts
            success = integrity == "ok" and counts_match
        finally:
            target.close()
        report = {
            "module_id": "P-011-XPIO-001", "test": "sqlite_backup_restore", "tested_at": utc_now(),
            "source_database": str(db_path), "backup_database": str(backup_path),
            "backup_sha256": sha256_file(backup_path), "integrity_check": integrity,
            "source_counts": source_counts, "backup_counts": backup_counts, "counts_match": counts_match,
            "status": "PASS" if success else "FAIL",
        }
        report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        cp.record_event(
            correlation_id="CORR-XPIO-20260822-BACKUP-RESTORE", actor_type="system", actor_id="XPIO-Q2-PROTOTYPE",
            platform_id="PLAT-MEPL", model_line="not_applicable", event_type="backup_restore_test",
            object_type="database", object_id=str(db_path), severity="INFO" if success else "CRITICAL",
            result="SUCCESS" if success else "FAILURE",
            summary="SQLite backup and restore integrity test passed" if success else "SQLite backup and restore integrity test failed",
            evidence_reference=str(report_path), details=report,
        )
        print(json.dumps(report, indent=2))
        return 0 if success else 1


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Prompt #11 XPIO Q2 control plane")
    sub = p.add_subparsers(dest="command", required=True)
    b = sub.add_parser("bootstrap", help="Initialize the database, import records, run diagnostics, and create reports")
    b.add_argument("--db", required=True)
    b.add_argument("--manifest", required=True)
    b.add_argument("--identity", required=True)
    b.add_argument("--work-packet", required=True)
    b.add_argument("--document", action="append", default=[], help="document_class=/path/to/file")
    b.add_argument("--json-report", required=True)
    b.add_argument("--markdown-report", required=True)
    b.set_defaults(func=bootstrap)
    d = sub.add_parser("diagnose", help="Re-run diagnostics and reports")
    d.add_argument("--db", required=True)
    d.add_argument("--json-report", required=True)
    d.add_argument("--markdown-report", required=True)
    d.set_defaults(func=command_diagnose)
    bt = sub.add_parser("backup-test", help="Create a SQLite backup and verify a restored copy")
    bt.add_argument("--db", required=True)
    bt.add_argument("--backup", required=True)
    bt.add_argument("--report", required=True)
    bt.set_defaults(func=command_backup_test)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return int(args.func(args))
    except (OSError, sqlite3.Error, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(json.dumps({"error": type(exc).__name__, "message": str(exc)}, indent=2), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
