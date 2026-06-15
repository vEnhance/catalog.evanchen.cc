#!/usr/bin/env python3
"""Update existing content/ frontmatter from a production dump.json.

This is the *ongoing* metadata sync (the one-time bootstrap was import_units.py).
It reads dump.json (pulled from the live server) and, for every unit page that
already exists in content/, refreshes only the fields the dump provides:

    name            -> title
    artist_name     -> extra.artist_name
    description      -> extra.description   (rewritten as a wrapped multi-line string)
    num_students    -> extra.num_students
    num_submissions -> extra.num_submissions
    num_clubs       -> extra.num_clubs
    num_hearts      -> extra.num_hearts     (rounded to a whole number)
    versions        -> extra.versions

Everything else in the frontmatter (unit_id, subject, classification, hidden,
in_search_index, ...) and the article body are preserved untouched. Pages with
no matching dump entry are left alone.
"""

import glob
import os
import re
import textwrap
import tomllib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DUMP = os.path.join(ROOT, "dump.json")
CONTENT = os.path.join(ROOT, "content")

FRONTMATTER_RE = re.compile(r"^\+\+\+\s*\n(.*?)\n\+\+\+\s*\n?(.*)$", re.DOTALL)

# Order in which [extra] keys are written (unknown keys are appended, preserved).
EXTRA_ORDER = [
    "unit_id",
    "subject",
    "classification",
    "artist_name",
    "num_students",
    "num_submissions",
    "num_clubs",
    "num_hearts",
    "versions",
    "hidden",
    "description",
]


def load_dump():
    import json

    with open(DUMP, encoding="utf-8") as f:
        groups = json.load(f)["unit_groups"]
    return {g["slug"]: g for g in groups}


# --- TOML emission ---------------------------------------------------------


def emit_basic(s):
    """A single-line TOML basic string (whitespace collapsed, escaped)."""
    s = re.sub(r"\s+", " ", s).strip()
    s = s.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{s}"'


def emit_description(s):
    """A wrapped multi-line string, so the .md source stays readable."""
    text = re.sub(r"\s+", " ", s).strip()
    wrapped = textwrap.fill(
        text, width=79, break_long_words=False, break_on_hyphens=False
    )
    if "'''" not in wrapped:
        # Literal multi-line string: no escaping, so LaTeX backslashes survive.
        return "'''\n" + wrapped + "'''"
    # Fallback (descriptions never contain ''' in practice).
    esc = wrapped.replace("\\", "\\\\").replace('"', '\\"')
    return '"""\n' + esc + '"""'


def emit_value(key, val):
    if key == "description" and isinstance(val, str):
        return emit_description(val)
    if isinstance(val, bool):
        return "true" if val else "false"
    if isinstance(val, int):
        return str(val)
    if isinstance(val, float):
        return repr(val)
    if isinstance(val, str):
        return emit_basic(val)
    if isinstance(val, list):
        return "[" + ", ".join(emit_basic(x) for x in val) + "]"
    raise TypeError(f"unhandled type for {key}: {type(val)}")


def serialize(data):
    lines = []
    top = ["title"] + [k for k in data if k not in ("title", "extra")]
    for k in top:
        if k in data:
            lines.append(f"{k} = {emit_value(k, data[k])}")
    lines.append("")
    lines.append("[extra]")
    extra = data.get("extra", {})
    seen = set()
    for k in EXTRA_ORDER:
        if k in extra:
            lines.append(f"{k} = {emit_value(k, extra[k])}")
            seen.add(k)
    for k in extra:
        if k not in seen:
            lines.append(f"{k} = {emit_value(k, extra[k])}")
    return "\n".join(lines)


# --- update ----------------------------------------------------------------


def apply_dump(data, entry):
    data["title"] = entry["name"]
    extra = data.setdefault("extra", {})
    extra["artist_name"] = entry["artist_name"]
    extra["description"] = entry["description"]
    extra["num_students"] = entry["num_students"]
    extra["num_submissions"] = entry["num_submissions"]
    extra["num_clubs"] = entry["num_clubs"]
    extra["num_hearts"] = round(entry["num_hearts"])
    extra["versions"] = entry["versions"]


def main():
    dump = load_dump()
    updated, skipped = 0, []
    for path in sorted(glob.glob(os.path.join(CONTENT, "*", "*.md"))):
        if os.path.basename(path) == "_index.md":
            continue
        slug = os.path.splitext(os.path.basename(path))[0]
        entry = dump.get(slug)
        if entry is None:
            skipped.append(slug)
            continue
        with open(path, encoding="utf-8") as f:
            text = f.read()
        m = FRONTMATTER_RE.match(text)
        if not m:
            skipped.append(slug + " (no frontmatter)")
            continue
        data = tomllib.loads(m.group(1))
        body = m.group(2)
        apply_dump(data, entry)
        with open(path, "w", encoding="utf-8") as f:
            f.write("+++\n" + serialize(data) + "\n+++\n" + body)
        updated += 1

    print(f"Updated {updated} unit page(s) from dump.json.")
    if skipped:
        print(f"No dump entry for {len(skipped)}: {skipped}")


if __name__ == "__main__":
    main()
