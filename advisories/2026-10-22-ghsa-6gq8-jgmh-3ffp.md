---
title: "GHSA-6gq8-jgmh-3ffp — npm nuxt"
date: "2026-10-22"
layout: post
category: "advisory"
osv_id: "GHSA-6gq8-jgmh-3ffp"
ecosystem: "npm"
packages: ["nuxt", "nuxt"]
cvss: 0
links: ["https://github.com/nuxt/nuxt/security/advisories/GHSA-6gq8-jgmh-3ffp", "https://nvd.nist.gov/vuln/detail/CVE-2026-114131", "https://github.com/nuxt/nuxt/commit/81f86ac5ee82bb1a9b887e59f3bc84624d711497", "https://github.com/nuxt/nuxt/commit/9123ed850c468a7424a868c20d0d49a5507d32e5", "https://github.com/nuxt/nuxt", "https://github.com/nuxt/nuxt/releases/tag/v3.21.11", "https://github.com/nuxt/nuxt/releases/tag/v4.5.2"]
tags: ["npm"]
---

Nuxt: Route rules are matched against the raw request path, so a percent-encoded segment can bypass `appMiddleware` on dynamic and catch-all routes

## References
- https://github.com/nuxt/nuxt/security/advisories/GHSA-6gq8-jgmh-3ffp
- https://nvd.nist.gov/vuln/detail/CVE-2026-114131
- https://github.com/nuxt/nuxt/commit/81f86ac5ee82bb1a9b887e59f3bc84624d711497
- https://github.com/nuxt/nuxt/commit/9123ed850c468a7424a868c20d0d49a5507d32e5
- https://github.com/nuxt/nuxt
- https://github.com/nuxt/nuxt/releases/tag/v3.21.11
- https://github.com/nuxt/nuxt/releases/tag/v4.5.2

