"""Apply reviewed date-only amendments to existing appointment records."""
import calendar
import copy
import json
import re
from pathlib import Path

REGISTER = Path(__file__).resolve().parents[1] / "data/careers/appointment-date-reconciliation.json"


def validate_date(value):
    if value is None:
        return
    if not isinstance(value, str) or not re.fullmatch(r"(?:19|20)\d{2}(?:-\d{2}(?:-\d{2})?)?", value):
        raise ValueError(f"Invalid date: {value!r}")
    parts = list(map(int, value.split("-")))
    if len(parts) > 1 and not 1 <= parts[1] <= 12:
        raise ValueError(f"Invalid month: {value}")
    if len(parts) > 2 and not 1 <= parts[2] <= calendar.monthrange(*parts[:2])[1]:
        raise ValueError(f"Invalid day: {value}")


def boundary(old, candidate):
    validate_date(old)
    validate_date(candidate)
    if candidate is None:
        return old, "unavailable"
    if old is None:
        return candidate, "added"
    if old == candidate or old.startswith(candidate + "-"):
        return old, "corroborated"
    if candidate.startswith(old + "-"):
        return candidate, "refined"
    return old, "conflict"


def reconcile(spell, amendment):
    for field, expected in amendment["expected"].items():
        if spell.get(field) != expected:
            raise ValueError(f"Stale appointment {amendment['spell_id']}: {field}")
    dates = amendment["indexed_dates"]
    start, start_status = boundary(spell.get("start_date"), dates["start_date"])
    end, end_status = boundary(spell.get("end_date"), dates["end_date"])
    conflict = "conflict" in (start_status, end_status)
    if conflict:
        start, end = spell.get("start_date"), spell.get("end_date")
    result = copy.deepcopy(spell)
    result.update(start_date=start, end_date=end)
    if (start, end) != (spell.get("start_date"), spell.get("end_date")):
        precision = { {4: "year", 7: "month", 10: "day"}[len(d)] for d in (start, end) if d }
        result["date_precision"] = next(iter(precision)) if len(precision) == 1 else "mixed" if precision else "unknown"
    warning = dates.get("end_label") == "Present" and spell.get("end_date") is not None
    result["appointment_date_evidence"] = {
        "indexed_dates": dates,
        "checked": amendment["checked"],
        "retrieval_method": amendment["retrieval_method"],
        "start_status": start_status,
        "end_status": end_status,
        "resolution": "held_conflict" if conflict else "reconciled",
        "closed_end_retained": warning,
    }
    return result


def apply_reconciliation(records, register=None):
    if register is None:
        if not REGISTER.exists():
            return records
        register = json.loads(REGISTER.read_text())
    amendments = {}
    for amendment in register["matches"]:
        key = (str(amendment["person_id"]), amendment["spell_id"])
        if key in amendments:
            raise ValueError(f"Duplicate appointment: {key}")
        for field in ("start_date", "end_date"):
            validate_date(amendment["indexed_dates"][field])
        amendments[key] = amendment
    result = copy.deepcopy(records)
    for record in result:
        for i, spell in enumerate(record["career_spells"]):
            amendment = amendments.get((str(record["person_id"]), spell["spell_id"]))
            if amendment:
                record["career_spells"][i] = reconcile(spell, amendment)
    return result
