---
title: "GHSA-hxh3-vqpv-xpqv — npm hono"
date: "2026-09-30"
layout: post
category: "advisory"
osv_id: "GHSA-hxh3-vqpv-xpqv"
ecosystem: "npm"
packages: ["hono"]
cvss: 0
links: ["https://github.com/honojs/hono/security/advisories/GHSA-hxh3-vqpv-xpqv", "https://nvd.nist.gov/vuln/detail/CVE-2026-93981", "https://github.com/honojs/hono/commit/2b8ed402cdab6dfc5e829b480806dcd8db94161e", "https://github.com/honojs/hono", "https://github.com/honojs/hono/releases/tag/v4.13.7", "https://www.vulncheck.com/advisories/hono-jsx-before-4.13.7-cross-site-scripting-via-unescaped-strings"]
tags: ["npm"]
---

hono/jsx renders plain strings unescaped in boundary components, leading to XSS

## References
- https://github.com/honojs/hono/security/advisories/GHSA-hxh3-vqpv-xpqv
- https://nvd.nist.gov/vuln/detail/CVE-2026-93981
- https://github.com/honojs/hono/commit/2b8ed402cdab6dfc5e829b480806dcd8db94161e
- https://github.com/honojs/hono
- https://github.com/honojs/hono/releases/tag/v4.13.7
- https://www.vulncheck.com/advisories/hono-jsx-before-4.13.7-cross-site-scripting-via-unescaped-strings

