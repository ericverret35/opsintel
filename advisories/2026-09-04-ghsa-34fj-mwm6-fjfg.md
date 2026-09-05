---
title: "GHSA-34fj-mwm6-fjfg — Go github.com/siyuan-note/siyuan/kernel"
date: "2026-09-04"
layout: post
category: "advisory"
osv_id: "GHSA-34fj-mwm6-fjfg"
ecosystem: "Go"
packages: ["github.com/siyuan-note/siyuan/kernel"]
cvss: 0
links: ["https://github.com/siyuan-note/siyuan/security/advisories/GHSA-34fj-mwm6-fjfg", "https://nvd.nist.gov/vuln/detail/CVE-2026-72794", "https://github.com/siyuan-note/siyuan/commit/77421530be4ab1f43310d0f50fbab05d16c38675", "https://github.com/siyuan-note/siyuan", "https://www.vulncheck.com/advisories/siyuan-before-session-cookie-key-disclosure-via-getconf"]
tags: ["go"]
---

SiYuan: The session-cookie signing key (Conf.CookieKey) is returned to anonymous readers by /api/system/getConf

## References
- https://github.com/siyuan-note/siyuan/security/advisories/GHSA-34fj-mwm6-fjfg
- https://nvd.nist.gov/vuln/detail/CVE-2026-72794
- https://github.com/siyuan-note/siyuan/commit/77421530be4ab1f43310d0f50fbab05d16c38675
- https://github.com/siyuan-note/siyuan
- https://www.vulncheck.com/advisories/siyuan-before-session-cookie-key-disclosure-via-getconf

