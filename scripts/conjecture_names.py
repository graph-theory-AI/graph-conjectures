"""Canonical PREFIX_english_name of each catalogue entry (data/conjecture_names.json).

Result files keyed by the old identifier (OPG slug, arXiv review id, bm_id,
others id) also carry the canonical name, placed right after `id`, so that they
can be read without the mapping at hand.
"""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

NAMES_FILE = Path(__file__).resolve().parent.parent / "data" / "conjecture_names.json"


@lru_cache(maxsize=None)
def names_by_id() -> dict[str, str]:
    doc = json.loads(NAMES_FILE.read_text(encoding="utf-8"))
    return {entry["id"]: entry["name"] for entry in doc["names"]}


def with_name(result: dict) -> dict:
    """Copy of `result` with its canonical `name` inserted after `id`.

    Ids that are not catalogue entries (e.g. in synthetic test fixtures) are
    left without a name.
    """
    name = names_by_id().get(result["id"])
    out = {}
    for key, value in result.items():
        if key == "name":
            continue
        out[key] = value
        if key == "id" and name:
            out["name"] = name
    return out
