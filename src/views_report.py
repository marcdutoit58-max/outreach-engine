#!/usr/bin/env python3
"""Mockup views per slug since a date. Reads a CSV export of the views table.
Usage: views_report.py views.csv [YYYY-MM-DD]"""
import csv, sys
from collections import defaultdict

since = sys.argv[2] if len(sys.argv) > 2 else "0000-00-00"
agg = defaultdict(list)
with open(sys.argv[1], newline="") as f:
    for r in csv.DictReader(f):
        if r["ts"] >= since and r.get("is_test", "0") == "0":
            agg[r["slug"]].append(r)
for slug, rows in sorted(agg.items(), key=lambda kv: max(x["ts"] for x in kv[1]), reverse=True):
    ts = sorted(x["ts"] for x in rows)
    print(f"{slug:<28} views={len(rows):<3} first={ts[0]}  last={ts[-1]}  -> FOLLOW UP")
