import json
import sqlite3
import tempfile
import unittest
from pathlib import Path

from xpio_control_plane import (
    XPIOControlPlane,
    privacy_route_allowed,
    release_eligible,
    sha256_file,
    stable_id,
)


class XPIOTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.db = self.root / "test.sqlite"
        self.artifact = self.root / "artifact.txt"
        self.artifact.write_text("Prompt 11 test artifact\n", encoding="utf-8")
        self.manifest = self.root / "manifest.json"
        sha = sha256_file(self.artifact)
        records = [
            {
                "artifact_id": "ART-P011-0001",
                "alias_name": "artifact.txt",
                "canonical_name": "artifact.txt",
                "original_path": str(self.artifact),
                "sha256": sha,
                "size_bytes": self.artifact.stat().st_size,
                "extension": ".txt",
                "category": "test",
                "duplicate_content": False,
                "registered_at": "2026-08-22T20:30:00-07:00",
                "privacy_class": "public",
                "status": "registered_build_input",
            },
            {
                "artifact_id": "ART-P011-0001",
                "alias_name": "artifact-copy.txt",
                "canonical_name": "artifact.txt",
                "original_path": str(self.artifact),
                "sha256": sha,
                "size_bytes": self.artifact.stat().st_size,
                "extension": ".txt",
                "category": "test",
                "duplicate_content": True,
                "registered_at": "2026-08-22T20:30:00-07:00",
                "privacy_class": "public",
                "status": "registered_build_input",
            },
        ]
        self.manifest.write_text(json.dumps({"artifacts": records}), encoding="utf-8")
        self.identity = self.root / "identity.json"
        self.identity.write_text(json.dumps({
            "identity_id": "CLONE-CEL-TEST",
            "identity_type": "ai_clone_interface",
            "display_name": "Test Clone",
            "human_owner": "Charles Earl Lipshay",
            "disclosure": "This is an AI interface and not the legal person.",
            "permitted_roles": ["test"],
            "permitted_memory_classes": ["project_record"],
            "prohibited_actions": [
                "impersonate the legal person",
                "fabricate personal memories",
                "move money",
                "sign contracts",
                "expand permissions",
                "pass HumanApprovalGate",
                "deploy its own mutations",
            ],
            "platform_scope": ["GitHub"],
            "status": "pilot",
            "human_approver": "Charles Earl Lipshay",
            "version": "0.1",
        }), encoding="utf-8")
        self.wp = self.root / "wp.json"
        self.wp.write_text(json.dumps({
            "work_packet_id": "WP-XPIO-0001",
            "correlation_id": "CORR-XPIO-TEST-0001",
            "title": "Test",
            "objective": "Test the XPIO control plane safely.",
            "human_owner": "Charles Earl Lipshay",
            "source_platform": "GitHub",
            "model_line": "chatgpt",
            "privacy_class": "public",
            "status": "review",
            "human_approval_status": "pending",
            "q_stage": "Q2",
            "risk_gate": "Yellow",
            "critical_gates_passed": False,
            "next_action": "Review",
        }), encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def make_cp(self):
        cp = XPIOControlPlane(self.db)
        cp.initialize()
        return cp

    def test_stable_id_is_deterministic(self):
        self.assertEqual(stable_id("TEST", "abc"), stable_id("TEST", "abc"))

    def test_database_initializes(self):
        with self.make_cp() as cp:
            tables = {r[0] for r in cp.conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
            self.assertIn("artifacts", tables)
            self.assertIn("events", tables)
            self.assertIn("diagnostics", tables)

    def test_artifact_manifest_imports_unique_and_alias_counts(self):
        with self.make_cp() as cp:
            unique, aliases = cp.import_artifact_manifest(self.manifest)
            self.assertEqual(unique, 1)
            self.assertEqual(aliases, 2)
            self.assertEqual(cp.conn.execute("SELECT COUNT(*) FROM artifacts").fetchone()[0], 1)
            self.assertEqual(cp.conn.execute("SELECT COUNT(*) FROM artifact_aliases").fetchone()[0], 2)

    def test_artifact_hash_passes(self):
        with self.make_cp() as cp:
            cp.import_artifact_manifest(self.manifest)
            results = cp.verify_artifacts()
            self.assertEqual(results[0].status, "PASS")

    def test_artifact_hash_mismatch_fails(self):
        with self.make_cp() as cp:
            cp.import_artifact_manifest(self.manifest)
            self.artifact.write_text("changed\n", encoding="utf-8")
            results = cp.verify_artifacts()
            self.assertEqual(results[0].status, "FAIL")

    def test_privacy_routing(self):
        self.assertTrue(privacy_route_allowed("public", "internal"))
        self.assertFalse(privacy_route_allowed("restricted", "internal"))

    def test_release_eligibility_requires_q4(self):
        ok, reasons = release_eligible("Q2", "Green", True, "approved", "human")
        self.assertFalse(ok)
        self.assertTrue(any("Q4" in r for r in reasons))

    def test_release_eligibility_rejects_ai_approver(self):
        ok, reasons = release_eligible("Q4", "Green", True, "approved", "ai_model")
        self.assertFalse(ok)
        self.assertTrue(any("not a human" in r for r in reasons))

    def test_identity_and_work_packet_import(self):
        with self.make_cp() as cp:
            self.assertEqual(cp.import_identity_passport(self.identity), "CLONE-CEL-TEST")
            self.assertEqual(cp.import_work_packet(self.wp), "WP-XPIO-0001")

    def test_event_requires_correlation_id(self):
        with self.make_cp() as cp:
            with self.assertRaises(ValueError):
                cp.record_event(
                    correlation_id="bad",
                    actor_type="system",
                    actor_id="test",
                    event_type="test",
                    object_type="test",
                    object_id="test",
                    severity="INFO",
                    result="SUCCESS",
                    summary="test",
                )

    def test_ai_cannot_pass_human_approval(self):
        with self.make_cp() as cp:
            with self.assertRaises(ValueError):
                cp.add_decision(
                    object_type="module",
                    object_id="P-011-XPIO-001",
                    decision="HumanApprovalGate approved",
                    rationale_summary="invalid",
                    approver_type="ai_model",
                    approver_id="CLONE-CEL-TEST",
                    status="approved",
                )

    def test_diagnostics_and_reports(self):
        with self.make_cp() as cp:
            cp.register_default_platforms()
            cp.import_artifact_manifest(self.manifest)
            cp.import_identity_passport(self.identity)
            cp.import_work_packet(self.wp)
            for name in ["canonical_architecture", "diagnostics_manual", "database_transparency", "identity_strategy", "artifact_vault"]:
                cp.register_document(self.artifact, name)
            cp.record_event(
                correlation_id="CORR-XPIO-TEST-0002",
                actor_type="system",
                actor_id="test",
                event_type="bootstrap",
                object_type="module",
                object_id="P-011-XPIO-001",
                severity="INFO",
                result="SUCCESS",
                summary="test bootstrap",
            )
            results = cp.run_diagnostics()
            cp.store_diagnostics(results)
            jp = self.root / "report.json"
            mp = self.root / "report.md"
            cp.write_reports(jp, mp)
            self.assertTrue(jp.exists())
            self.assertTrue(mp.exists())
            report = json.loads(jp.read_text(encoding="utf-8"))
            self.assertEqual(report["counts"]["artifacts"], 1)
            self.assertEqual(report["q_stage"], "Q2")

    def test_sqlite_integrity(self):
        with self.make_cp() as cp:
            self.assertEqual(cp.conn.execute("PRAGMA integrity_check").fetchone()[0], "ok")

    def test_backup_restore_event_changes_diagnostic_to_pass(self):
        with self.make_cp() as cp:
            cp.record_event(
                correlation_id="CORR-XPIO-BACKUP-TEST",
                actor_type="system",
                actor_id="test",
                event_type="backup_restore_test",
                object_type="database",
                object_id=str(self.db),
                severity="INFO",
                result="SUCCESS",
                summary="backup passed",
            )
            result = [r for r in cp.run_diagnostics() if r.check_name == "backup_restore_evidence"][0]
            self.assertEqual(result.status, "PASS")


if __name__ == "__main__":
    unittest.main(verbosity=2)
