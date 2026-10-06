---
title: "GHSA-r273-hxvj-fxhp — npm vm2"
date: "2026-10-05"
layout: post
category: "advisory"
osv_id: "GHSA-r273-hxvj-fxhp"
ecosystem: "npm"
packages: ["vm2"]
cvss: 0
links: ["https://github.com/patriksimek/vm2/security/advisories/GHSA-r273-hxvj-fxhp", "https://nvd.nist.gov/vuln/detail/CVE-2026-92933", "https://github.com/patriksimek/vm2/commit/e10bd2f539ab1a90c2d37466e6aae740d4a1ce2a", "https://github.com/patriksimek/vm2", "https://github.com/patriksimek/vm2/releases/tag/v3.11.8", "https://www.vulncheck.com/advisories/vm2-before-3.11.8-information-disclosure-via-util-getcallsites"]
tags: ["npm"]
---

vm2: util.getCallSites() bypasses GHSA-v27g-jcqj-v8rw host-frame redaction, leaks host call stack

## References
- https://github.com/patriksimek/vm2/security/advisories/GHSA-r273-hxvj-fxhp
- https://nvd.nist.gov/vuln/detail/CVE-2026-92933
- https://github.com/patriksimek/vm2/commit/e10bd2f539ab1a90c2d37466e6aae740d4a1ce2a
- https://github.com/patriksimek/vm2
- https://github.com/patriksimek/vm2/releases/tag/v3.11.8
- https://www.vulncheck.com/advisories/vm2-before-3.11.8-information-disclosure-via-util-getcallsites

