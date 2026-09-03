import json
import tempfile
import unittest
from pathlib import Path

from idea_ledger import IdeaLedger, Priority, QualityState, Status


class IdeaLedgerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.ledger = IdeaLedger()

    def test_create_and_get(self) -> None:
        idea = self.ledger.create(
            title="Build reading tracker",
            description="Track books and notes",
            category="learning",
            priority=Priority.HIGH,
            tags=["python", "learning", "python"],
        )
        fetched = self.ledger.get(idea.idea_id)
        self.assertEqual(fetched.title, "Build reading tracker")
        self.assertEqual(fetched.priority, Priority.HIGH)
        self.assertEqual(fetched.tags, ("python", "learning"))

    def test_empty_required_fields_fail(self) -> None:
        with self.assertRaises(ValueError):
            self.ledger.create(title=" ", description="x", category="y")

    def test_list_filters_and_archive_default(self) -> None:
        a = self.ledger.create(title="A", description="a", category="dev")
        b = self.ledger.create(title="B", description="b", category="Dev", priority=Priority.HIGH)
        self.ledger.update(a.idea_id, status=Status.BUILDING)
        self.ledger.archive(b.idea_id)

        visible = self.ledger.list(category="DEV")
        self.assertEqual([item.idea_id for item in visible], [a.idea_id])

        archived = self.ledger.list(include_archived=True, status=Status.ARCHIVED)
        self.assertEqual([item.idea_id for item in archived], [b.idea_id])

    def test_update_and_note(self) -> None:
        idea = self.ledger.create(title="A", description="a", category="dev")
        updated = self.ledger.update(
            idea.idea_id,
            status=Status.TESTING,
            quality_state=QualityState.REVIEW,
        )
        self.assertEqual(updated.status, Status.TESTING)
        self.assertEqual(updated.quality_state, QualityState.REVIEW)

        noted = self.ledger.add_note(idea.idea_id, "Add export tests")
        self.assertEqual(noted.notes[-1], "Add export tests")

    def test_archived_idea_cannot_be_reactivated_by_generic_update(self) -> None:
        idea = self.ledger.create(title="A", description="a", category="dev")
        self.ledger.archive(idea.idea_id)
        with self.assertRaises(ValueError):
            self.ledger.update(idea.idea_id, status=Status.BUILDING)

    def test_export_import_round_trip(self) -> None:
        idea = self.ledger.create(
            title="Ledger",
            description="Deterministic baseline",
            category="pilot",
            tags=["benchmark"],
        )
        self.ledger.add_note(idea.idea_id, "round-trip")

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "ledger.json"
            self.ledger.export_json(path)
            restored = IdeaLedger.import_json(path)

            self.assertEqual(restored.get(idea.idea_id).to_dict(), self.ledger.get(idea.idea_id).to_dict())

    def test_import_rejects_bad_schema_version(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "ledger.json"
            path.write_text(json.dumps({"schema_version": 99, "ideas": []}), encoding="utf-8")
            with self.assertRaises(ValueError):
                IdeaLedger.import_json(path)

    def test_health_check_green(self) -> None:
        self.ledger.create(title="A", description="a", category="dev")
        report = self.ledger.health_check()
        self.assertEqual(report["status"], "GREEN")
        self.assertEqual(report["errors"], [])


if __name__ == "__main__":
    unittest.main()
