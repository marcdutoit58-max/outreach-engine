CREATE TABLE IF NOT EXISTS mockup_views (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ts TEXT NOT NULL,           -- UTC ISO time
  slug TEXT NOT NULL,
  country TEXT,
  ua TEXT,
  is_test INTEGER DEFAULT 0   -- owner/test views excluded from reports
);
CREATE INDEX IF NOT EXISTS idx_views_slug_ts ON mockup_views (slug, ts);
