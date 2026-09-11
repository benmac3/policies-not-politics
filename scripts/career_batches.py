"""Resolve deterministic Parliament career-research batches from the frozen roster."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load():
    parliament = json.loads((ROOT / "data/parliament.json").read_text())
    plan = json.loads((ROOT / "data/career-batch-plan.json").read_text())
    return parliament["roster"], plan


def resolve(roster, batch):
    members = sorted((r for r in roster if r.get("state") == batch["state"]), key=lambda r: r["name"])
    selected = members[batch["start"]:batch["end"]]
    if len(selected) != batch["expected_members"]:
        raise SystemExit(
            f"{batch['id']}: expected {batch['expected_members']} members but selected {len(selected)}; "
            "the roster or batch plan changed"
        )
    return selected


def check(roster, plan):
    assigned = []
    for batch in plan["batches"]:
        assigned.extend((m["id"], batch["id"]) for m in resolve(roster, batch))
    ids = [x[0] for x in assigned]
    roster_ids = [r["id"] for r in roster]
    duplicate_ids = sorted({i for i in ids if ids.count(i) > 1})
    missing_ids = sorted(set(roster_ids) - set(ids))
    extra_ids = sorted(set(ids) - set(roster_ids))
    if duplicate_ids or missing_ids or extra_ids or len(ids) != len(roster_ids):
        raise SystemExit(
            f"Batch coverage failed: assigned={len(ids)} roster={len(roster_ids)} "
            f"duplicates={duplicate_ids} missing={missing_ids} extra={extra_ids}"
        )
    print(f"PASS: {len(roster_ids)} parliamentarians assigned exactly once across {len(plan['batches'])} batches")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", help="Batch id, e.g. nsw-1")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--json", action="store_true", help="Emit selected members as JSON")
    args = parser.parse_args()

    roster, plan = load()
    if args.check:
        check(roster, plan)
    if args.batch:
        try:
            batch = next(b for b in plan["batches"] if b["id"] == args.batch)
        except StopIteration:
            raise SystemExit(f"Unknown batch: {args.batch}")
        members = resolve(roster, batch)
        if args.json:
            print(json.dumps(members, ensure_ascii=False, indent=2))
        else:
            for index, member in enumerate(members, 1):
                print(f"{index:02d}. {member['id']} | {member['name']} | {member['chamber']} | {member['party']}")

    if not args.check and not args.batch:
        parser.error("use --check and/or --batch BATCH_ID")


if __name__ == "__main__":
    main()
