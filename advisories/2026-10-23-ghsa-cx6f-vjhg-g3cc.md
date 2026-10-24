---
title: "GHSA-cx6f-vjhg-g3cc — PyPI virtualenv"
date: "2026-10-23"
layout: post
category: "advisory"
osv_id: "GHSA-cx6f-vjhg-g3cc"
ecosystem: "PyPI"
packages: ["virtualenv"]
cvss: 0
links: ["https://github.com/pypa/virtualenv/security/advisories/GHSA-cx6f-vjhg-g3cc", "https://github.com/pypa/virtualenv/pull/3466", "https://github.com/pypa/virtualenv/commit/3598e201f6f044e389136b2347a8a919ac03c5f4", "https://github.com/pypa/virtualenv", "https://github.com/pypa/virtualenv/releases/tag/21.14.13"]
tags: ["pypi"]
---

virtualenv: Bash activator leaves the --prompt value unescaped in PS1 when promptvars is off, so prompt expansion later executes it (regression in 21.14.9)

## References
- https://github.com/pypa/virtualenv/security/advisories/GHSA-cx6f-vjhg-g3cc
- https://github.com/pypa/virtualenv/pull/3466
- https://github.com/pypa/virtualenv/commit/3598e201f6f044e389136b2347a8a919ac03c5f4
- https://github.com/pypa/virtualenv
- https://github.com/pypa/virtualenv/releases/tag/21.14.13

