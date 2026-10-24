# Outreach Engine - case study

A small, low-cost pipeline I built to find local businesses with weak or missing websites, show each one a personalised mockup of a better site, and follow up only with the ones who actually looked.

Built and run by Marc du Toit, EFS Digital | www.efsdigital.co.za

## Problem
Cold outreach for small web projects usually means generic emails, no way to tell who is interested, and follow-ups sent blind. I wanted every first message to carry something specific to that business, and every follow-up to be driven by a real signal.

## How it works
1. **Source** - public business listings for a town and trade are collected into a CSV (name, trade, town, website or none).
2. **Qualify** - each lead is scored: no website, not mobile-friendly, no HTTPS, no clear call-to-action, no booking/contact form. Higher score = bigger visible gap.
3. **Mockup** - for qualified leads a one-page mockup is generated from a template per trade and published at a private, unindexed URL with a short slug.
4. **Message** - a short, plain message per lead: what was noticed, the mockup link, one question. One channel per lead, capped daily volumes.
5. **Track** - the mockup page fires a tiny beacon to an edge worker that writes `slug, time, country` to a database. Test and owner views are flagged and excluded.
6. **Follow up** - a report lists who opened their mockup and when. Only viewers get a follow-up; non-viewers get at most one gentle nudge, then are dropped.
7. **Close** - fixed-price offer, deposit, then the real site goes live on the same template.

## Rules built in
- Daily send caps and one channel per lead.
- Clear opt-out in every message; opted-out leads are never contacted again.
- No personal data beyond what the business publishes; mockup pages are noindex.
- Human review before any message goes out.

## Stack
- Python scripts for sourcing, scoring and reporting (`src/`)
- Static mockup pages on an edge host, noindex
- Edge worker + SQL database for view tracking (`worker/`)
- Spreadsheet/CRM for pipeline status

Running cost: roughly the price of a basic edge-hosting plan (about US$5/month).

## What it showed
- Leads who open the mockup are the only ones worth a second message; this cut follow-up volume sharply.
- Follow-ups are timed off the view itself rather than a fixed day count.
- A specific mockup beats a generic pitch: replies ask about price and timing, not "what is this?".

## Repo contents
- `src/score_leads.py` - lead qualification scoring
- `src/views_report.py` - who viewed which mockup, since a date
- `worker/beacon.js` - edge worker that records mockup views
- `worker/schema.sql` - views table
- `sample-data/leads_sample.csv` - fictional sample leads
- `docs/flow.md` - pipeline diagram

All data in this repo is fictional.
