"""Validate and aggregate per-member parliamentary career research records."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MEMBERS = ROOT / "data/careers/members"

REQUIRED_TOP = {
    "person_id", "name", "snapshot_state", "snapshot_chamber", "snapshot_party",
    "snapshot_source", "research_status", "last_reviewed", "headline",
    "career_spells", "sources", "research_notes"
}


def load_records():
    if not MEMBERS.exists():
        return []
    records = []
    for path in sorted(MEMBERS.glob("*.json")):
        record = json.loads(path.read_text())
        missing = sorted(REQUIRED_TOP - set(record))
        if missing:
            raise SystemExit(f"{path}: missing required fields {missing}")
        if path.stem != str(record["person_id"]):
            raise SystemExit(f"{path}: filename must equal person_id {record['person_id']}")
        records.append(record)
    ids = [r["person_id"] for r in records]
    if len(ids) != len(set(ids)):
        raise SystemExit("Duplicate person_id in career records")
    return records


def main():
    records = load_records()
    summary = []
    spells = []
    for record in records:
        headline = record.get("headline", {})
        summary.append({
            "person_id": record["person_id"],
            "name": record["name"],
            "state": record["snapshot_state"],
            "chamber": record["snapshot_chamber"],
            "party": record["snapshot_party"],
            "research_status": record["research_status"],
            "public_full_time_years": headline.get("public_full_time_years"),
            "private_full_time_years": headline.get("private_full_time_years"),
            "calculation_status": headline.get("calculation_status"),
            "calculation_note": headline.get("note", "")
        })
        for spell in record.get("career_spells", []):
            row = dict(spell)
            row["person_id"] = record["person_id"]
            row["name"] = record["name"]
            spells.append(row)

    (ROOT / "data/career-summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    (ROOT / "data/career-spells.json").write_text(json.dumps(spells, ensure_ascii=False, indent=2) + "\n")

    with (ROOT / "data/career-summary.csv").open("w", newline="") as f:
        fields = [
            "person_id", "name", "state", "chamber", "party", "research_status",
            "public_full_time_years", "private_full_time_years", "calculation_status", "calculation_note"
        ]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(summary)

    spell_fields = [
        "person_id", "name", "spell_id", "employer", "role", "start_date", "end_date",
        "date_precision", "employment_status", "fte_fraction", "category", "headline_sector",
        "government_control_at_time", "counting_status", "source_ids", "evidence_note", "counting_note"
    ]
    with (ROOT / "data/career-spells.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=spell_fields, extrasaction="ignore")
        writer.writeheader()
        for row in spells:
            out = dict(row)
            if isinstance(out.get("source_ids"), list):
                out["source_ids"] = ";".join(out["source_ids"])
            writer.writerow(out)

    print(f"Built {len(summary)} member summaries and {len(spells)} career spells")


if __name__ == "__main__":
    main()
