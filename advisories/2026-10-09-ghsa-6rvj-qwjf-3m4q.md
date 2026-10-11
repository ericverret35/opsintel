---
title: "GHSA-6rvj-qwjf-3m4q — Go code.vikunja.io/api"
date: "2026-10-09"
layout: post
category: "advisory"
osv_id: "GHSA-6rvj-qwjf-3m4q"
ecosystem: "Go"
packages: ["code.vikunja.io/api"]
cvss: 0
links: ["https://github.com/go-vikunja/vikunja/security/advisories/GHSA-6rvj-qwjf-3m4q", "https://nvd.nist.gov/vuln/detail/CVE-2026-91972", "https://github.com/go-vikunja/vikunja", "https://github.com/go-vikunja/vikunja/releases/tag/v2.6.0", "https://www.vulncheck.com/advisories/vikunja-before-2.6.0-authentication-bypass-via-unthrottled-api"]
tags: ["go"]
---

Vikunja: Every /api/v2 pre-auth endpoint is unthrottled on a stock install while its /api/v1 twin is rate limited

## References
- https://github.com/go-vikunja/vikunja/security/advisories/GHSA-6rvj-qwjf-3m4q
- https://nvd.nist.gov/vuln/detail/CVE-2026-91972
- https://github.com/go-vikunja/vikunja
- https://github.com/go-vikunja/vikunja/releases/tag/v2.6.0
- https://www.vulncheck.com/advisories/vikunja-before-2.6.0-authentication-bypass-via-unthrottled-api

