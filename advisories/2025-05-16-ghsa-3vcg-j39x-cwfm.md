---
title: "GHSA-3vcg-j39x-cwfm — PyPI vyper"
date: "2025-05-16"
layout: post
category: "advisory"
osv_id: "GHSA-3vcg-j39x-cwfm"
ecosystem: "PyPI"
packages: ["vyper"]
cvss: 0
links: ["https://github.com/vyperlang/vyper/security/advisories/GHSA-3vcg-j39x-cwfm", "https://nvd.nist.gov/vuln/detail/CVE-2025-47774", "https://github.com/vyperlang/vyper/pull/4645", "https://github.com/vyperlang/vyper", "https://github.com/vyperlang/vyper/blob/68b68c4b30c5ef2f312b4674676170b8a6eaa316/vyper/builtins/functions.py#L315-L319", "https://github.com/vyperlang/vyper/blob/68b68c4b30c5ef2f312b4674676170b8a6eaa316/vyper/codegen/core.py#L189-L191"]
tags: ["pypi"]
---

Vyper's `slice()` may elide side-effects when output length is 0

## References
- https://github.com/vyperlang/vyper/security/advisories/GHSA-3vcg-j39x-cwfm
- https://nvd.nist.gov/vuln/detail/CVE-2025-47774
- https://github.com/vyperlang/vyper/pull/4645
- https://github.com/vyperlang/vyper
- https://github.com/vyperlang/vyper/blob/68b68c4b30c5ef2f312b4674676170b8a6eaa316/vyper/builtins/functions.py#L315-L319
- https://github.com/vyperlang/vyper/blob/68b68c4b30c5ef2f312b4674676170b8a6eaa316/vyper/codegen/core.py#L189-L191

