#!/usr/bin/env python3
"""Score leads by visible website gaps. Usage: score_leads.py leads.csv [min_score]"""
import csv, sys

WEIGHTS = {"no_website": 5, "no_https": 2, "not_mobile": 3, "no_cta": 2, "no_contact_form": 1}

def score(row):
    if not row.get("website"):
        return WEIGHTS["no_website"], ["no_website"]
    gaps = [k for k in WEIGHTS if k != "no_website" and row.get(k, "").strip().lower() in ("1", "yes", "true")]
    return sum(WEIGHTS[g] for g in gaps), gaps

def main():
    path = sys.argv[1]
    min_score = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    scored = sorted(((score(r), r) for r in rows), key=lambda x: -x[0][0])
    for (s, gaps), r in scored:
        flag = "QUALIFIED" if s >= min_score else "skip"
        print(f"{s:>2}  {flag:<9} {r['business']} ({r['trade']}, {r['town']})  gaps: {', '.join(gaps) or '-'}")

if __name__ == "__main__":
    main()
