---
title: "GHSA-j3hm-6rg5-mchv — npm vm2"
date: "2026-10-05"
layout: post
category: "advisory"
osv_id: "GHSA-j3hm-6rg5-mchv"
ecosystem: "npm"
packages: ["vm2"]
cvss: 0
links: ["https://github.com/patriksimek/vm2/security/advisories/GHSA-j3hm-6rg5-mchv", "https://nvd.nist.gov/vuln/detail/CVE-2026-92946", "https://github.com/patriksimek/vm2/commit/903017c8a1eae9aba947ec854468b48155e79f86", "https://github.com/patriksimek/vm2", "https://github.com/patriksimek/vm2/releases/tag/v3.11.7", "https://www.vulncheck.com/advisories/vm2-before-3.11.7-remote-code-execution-via-require-external"]
tags: ["npm"]
---

vm2: NodeVM `require.external` without an explicit `require.root` grants unrestricted host filesystem access and full RCE

## References
- https://github.com/patriksimek/vm2/security/advisories/GHSA-j3hm-6rg5-mchv
- https://nvd.nist.gov/vuln/detail/CVE-2026-92946
- https://github.com/patriksimek/vm2/commit/903017c8a1eae9aba947ec854468b48155e79f86
- https://github.com/patriksimek/vm2
- https://github.com/patriksimek/vm2/releases/tag/v3.11.7
- https://www.vulncheck.com/advisories/vm2-before-3.11.7-remote-code-execution-via-require-external

