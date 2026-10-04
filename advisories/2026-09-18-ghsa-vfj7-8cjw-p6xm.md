---
title: "GHSA-vfj7-8cjw-p6xm — npm braces"
date: "2026-09-18"
layout: post
category: "advisory"
osv_id: "GHSA-vfj7-8cjw-p6xm"
ecosystem: "npm"
packages: ["braces"]
cvss: 0
links: ["https://nvd.nist.gov/vuln/detail/CVE-2026-93687", "https://github.com/micromatch/braces/issues/70", "https://github.com/micromatch/braces", "https://github.com/micromatch/braces/blob/3.0.3/lib/compile.js#L49-L53", "https://github.com/micromatch/braces/blob/3.0.3/lib/expand.js#L102-L105", "https://github.com/micromatch/braces/blob/3.0.3/lib/parse.js#L38-L40", "https://www.vulncheck.com/advisories/braces-through-3.0.3-stack-overflow-via-deeply-nested-patterns"]
tags: ["npm"]
---

braces vulnerable to stack-exhaustion denial of service through deeply nested patterns

## References
- https://nvd.nist.gov/vuln/detail/CVE-2026-93687
- https://github.com/micromatch/braces/issues/70
- https://github.com/micromatch/braces
- https://github.com/micromatch/braces/blob/3.0.3/lib/compile.js#L49-L53
- https://github.com/micromatch/braces/blob/3.0.3/lib/expand.js#L102-L105
- https://github.com/micromatch/braces/blob/3.0.3/lib/parse.js#L38-L40
- https://www.vulncheck.com/advisories/braces-through-3.0.3-stack-overflow-via-deeply-nested-patterns

