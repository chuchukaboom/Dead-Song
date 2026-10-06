#!/usr/bin/env python3
"""Preflight for the run-based Silksong mod design sheets.

Lays every sheet's rows and columns over each other and lists:
  - rows missing a column, or carrying an extra one
  - cells that are null where a value is required
  - references between sheets that do not resolve
  - rows whose status is not yet verified/decided
Run from this folder:  python3 preflight.py
Build only when the report is clean.
"""
import json
import pathlib
import sys

here = pathlib.Path(__file__).parent
names = ["loadouts", "loot_items", "hooks", "run_rules"]
sheets = {n: json.loads((here / f"{n}.json").read_text()) for n in names}

# Columns allowed to be null on purpose
NULLABLE = {"loadouts": {"startItemId"}, "loot_items": set(), "hooks": set(), "run_rules": set()}
DONE_STATUS = {"verified", "decided"}

findings = {"structure": [], "unfilled": [], "references": [], "status": []}

ids = {n: {r["id"] for r in s["rows"]} for n, s in sheets.items()}

for n, s in sheets.items():
    cols = set(s["columns"])
    for r in s["rows"]:
        rid = f'{n}:{r.get("id", "?")}'
        keys = set(r)
        for c in sorted(cols - keys):
            findings["structure"].append(f"{rid} is missing column '{c}'")
        for c in sorted(keys - cols):
            findings["structure"].append(f"{rid} has extra column '{c}'")
        for c in s["columns"]:
            if c in r and r[c] is None and c not in NULLABLE[n]:
                findings["unfilled"].append(f"{rid}.{c} is empty")
        if r.get("status") not in DONE_STATUS:
            findings["status"].append(f"{rid} status is '{r.get('status')}'")

# Cross-sheet references
for r in sheets["loadouts"]["rows"]:
    if r["startItemId"] is not None and r["startItemId"] not in ids["loot_items"]:
        findings["references"].append(f"loadouts:{r['id']}.startItemId -> {r['startItemId']} not in loot_items")
for r in sheets["loot_items"]["rows"]:
    for h in r["hooks"]:
        if h not in ids["hooks"]:
            findings["references"].append(f"loot_items:{r['id']}.hooks -> {h} not in hooks")
for r in sheets["run_rules"]["rows"]:
    for h in r["hooks"]:
        if h not in ids["hooks"]:
            findings["references"].append(f"run_rules:{r['id']}.hooks -> {h} not in hooks")
for r in sheets["hooks"]["rows"]:
    for u in r["usedBy"]:
        if u != "core" and u not in ids["loot_items"]:
            findings["references"].append(f"hooks:{r['id']}.usedBy -> {u} not in loot_items")
        if u != "core" and u in ids["loot_items"]:
            item = next(i for i in sheets["loot_items"]["rows"] if i["id"] == u)
            if r["id"] not in item["hooks"]:
                findings["references"].append(f"hooks:{r['id']} says {u} uses it, but {u}.hooks does not list it")

# Hooks nothing uses
used = {h for i in sheets["loot_items"]["rows"] for h in i["hooks"]} | {h for i in sheets["run_rules"]["rows"] for h in i["hooks"]}
for r in sheets["hooks"]["rows"]:
    if r["id"] not in used and "core" not in r["usedBy"]:
        findings["references"].append(f"hooks:{r['id']} is not used by anything")

# Unresolved game targets and game refs
unresolved = []
for r in sheets["hooks"]["rows"]:
    if r["gameTarget"] is None:
        unresolved.append(f"hooks:{r['id']} ({r['name']}) has no gameTarget yet")
for r in sheets["loadouts"]["rows"]:
    unresolved.append(f"loadouts:{r['id']} crest/tool names not yet matched to game data")

print("PREFLIGHT REPORT")
print("=" * 40)
for k in ["structure", "unfilled", "references", "status"]:
    print(f"\n[{k}] {len(findings[k])} finding(s)")
    for f in findings[k]:
        print("  -", f)
print(f"\n[game links] {len(unresolved)} still to resolve against Silksong's code/data")
for f in unresolved:
    print("  -", f)

blocking = sum(len(v) for k, v in findings.items() if k in ("structure", "unfilled", "references"))
print("\n" + "=" * 40)
if blocking == 0 and not unresolved:
    print("CLEAN: ok to build.")
else:
    print(f"NOT READY: {blocking} sheet problem(s), {len(unresolved)} game link(s) unresolved.")
sys.exit(0 if blocking == 0 and not unresolved else 1)
