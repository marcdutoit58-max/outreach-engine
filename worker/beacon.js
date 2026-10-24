// Edge worker: records a mockup view. Page calls: fetch('/v?s=<slug>', {method:'POST', keepalive:true})
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname !== "/v" || request.method !== "POST") return new Response("Not found", { status: 404 });
    const slug = (url.searchParams.get("s") || "").replace(/[^a-z0-9-]/g, "").slice(0, 60);
    if (!slug) return new Response("Bad slug", { status: 400 });
    const isTest = url.searchParams.get("t") === env.TEST_KEY ? 1 : 0;
    await env.DB.prepare("INSERT INTO mockup_views (ts, slug, country, ua, is_test) VALUES (?, ?, ?, ?, ?)")
      .bind(new Date().toISOString(), slug, request.cf?.country || null,
            (request.headers.get("user-agent") || "").slice(0, 200), isTest)
      .run();
    return new Response(null, { status: 204 });
  },
};
