---
title: "GHSA-2qqv-3jgq-vpm9 — Go github.com/siyuan-note/siyuan/kernel"
date: "2026-08-12"
layout: post
category: "advisory"
osv_id: "GHSA-2qqv-3jgq-vpm9"
ecosystem: "Go"
packages: ["github.com/siyuan-note/siyuan/kernel"]
cvss: 0
links: ["https://github.com/siyuan-note/siyuan/security/advisories/GHSA-h4v5-crx2-3cv4", "https://nvd.nist.gov/vuln/detail/CVE-2026-72793", "https://www.vulncheck.com/advisories/siyuan-before-information-disclosure-via-api-system-getconf"]
tags: ["go"]
---

Duplicate Advisory: Non-administrator responses from /api/system/getConf omit three secrets that the configuration-export path explicitly strips, disclosing the session-cookie signing key and the OS username to anonymous readers

## References
- https://github.com/siyuan-note/siyuan/security/advisories/GHSA-h4v5-crx2-3cv4
- https://nvd.nist.gov/vuln/detail/CVE-2026-72793
- https://www.vulncheck.com/advisories/siyuan-before-information-disclosure-via-api-system-getconf

