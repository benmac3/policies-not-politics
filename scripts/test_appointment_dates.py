"""Focused checks for safe date-only reconciliation."""
import unittest
from reconcile_appointment_dates import apply_reconciliation, boundary, reconcile


class AppointmentDatesTest(unittest.TestCase):
    def fixture(self, start="2020", end="2021"):
        spell = {"spell_id": "p-1", "employer": "Existing employer", "role": "Existing role",
                 "start_date": start, "end_date": end, "date_precision": "year",
                 "fte_fraction": None, "counting_status": "insufficient_evidence"}
        amendment = {"person_id": "p", "spell_id": "p-1", "expected": dict(spell),
                     "indexed_dates": {"start_date": "2020-02", "end_date": "2021-03", "end_label": None},
                     "checked": "2026-10-15", "retrieval_method": "public_search_index"}
        return spell, amendment

    def test_more_precise_existing_date(self):
        self.assertEqual(boundary("2020-02-11", "2020-02"), ("2020-02-11", "corroborated"))

    def test_refinement_changes_only_dates(self):
        spell, amendment = self.fixture()
        result = reconcile(spell, amendment)
        self.assertEqual(result["start_date"], "2020-02")
        self.assertEqual(result["end_date"], "2021-03")
        self.assertEqual(result["date_precision"], "month")
        for key in ("employer", "role", "fte_fraction", "counting_status"):
            self.assertEqual(result[key], spell[key])
        self.assertEqual(spell["start_date"], "2020")

    def test_conflict_holds_entire_pair(self):
        spell, amendment = self.fixture()
        amendment["indexed_dates"]["end_date"] = "2022"
        result = reconcile(spell, amendment)
        self.assertEqual((result["start_date"], result["end_date"]), ("2020", "2021"))
        self.assertEqual(result["appointment_date_evidence"]["resolution"], "held_conflict")

    def test_present_never_clears_end(self):
        spell, amendment = self.fixture()
        amendment["indexed_dates"].update(end_date=None, end_label="Present")
        result = reconcile(spell, amendment)
        self.assertEqual(result["end_date"], "2021")
        self.assertTrue(result["appointment_date_evidence"]["closed_end_retained"])

    def test_stale_record_rejected(self):
        spell, amendment = self.fixture()
        spell["role"] = "Changed role"
        with self.assertRaises(ValueError):
            reconcile(spell, amendment)

    def test_duplicate_target_rejected_and_absent_members_skipped(self):
        _, amendment = self.fixture()
        self.assertEqual(apply_reconciliation([], {"matches": [amendment]}), [])
        with self.assertRaises(ValueError):
            apply_reconciliation([], {"matches": [amendment, amendment]})


if __name__ == "__main__":
    unittest.main()
