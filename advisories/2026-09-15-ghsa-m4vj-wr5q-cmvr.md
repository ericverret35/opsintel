---
title: "GHSA-m4vj-wr5q-cmvr — Go github.com/go-vikunja/vikunja"
date: "2026-09-15"
layout: post
category: "advisory"
osv_id: "GHSA-m4vj-wr5q-cmvr"
ecosystem: "Go"
packages: ["github.com/go-vikunja/vikunja"]
cvss: 0
links: ["https://github.com/go-vikunja/vikunja/security/advisories/GHSA-6rvj-qwjf-3m4q", "https://nvd.nist.gov/vuln/detail/CVE-2026-91972", "https://www.vulncheck.com/advisories/vikunja-before-2.6.0-authentication-bypass-via-unthrottled-api"]
tags: ["go"]
---

Duplicate Advisory: Vikunja: Every /api/v2 pre-auth endpoint is unthrottled on a stock install while its /api/v1 twin is rate limited

## References
- https://github.com/go-vikunja/vikunja/security/advisories/GHSA-6rvj-qwjf-3m4q
- https://nvd.nist.gov/vuln/detail/CVE-2026-91972
- https://www.vulncheck.com/advisories/vikunja-before-2.6.0-authentication-bypass-via-unthrottled-api

