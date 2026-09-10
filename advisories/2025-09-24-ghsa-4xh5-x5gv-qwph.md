---
title: "GHSA-4xh5-x5gv-qwph — PyPI pip"
date: "2025-09-24"
layout: post
category: "advisory"
osv_id: "GHSA-4xh5-x5gv-qwph"
ecosystem: "PyPI"
packages: ["pip"]
cvss: 0
links: ["https://nvd.nist.gov/vuln/detail/CVE-2025-8869", "https://github.com/pypa/pip/pull/13550", "https://github.com/pypa/pip/commit/f2b92314da012b9fffa36b3f3e67748a37ef464a", "https://github.com/pypa/pip", "https://lists.debian.org/debian-lts-announce/2025/10/msg00028.html", "https://mail.python.org/archives/list/security-announce@python.org/thread/IF5A3GCJY3VH7BVHJKOWOJFKTW7VFQEN", "https://pip.pypa.io/en/stable/news/#v25-2"]
tags: ["pypi"]
---

pip's fallback tar extraction doesn't check symbolic links point to extraction directory

## References
- https://nvd.nist.gov/vuln/detail/CVE-2025-8869
- https://github.com/pypa/pip/pull/13550
- https://github.com/pypa/pip/commit/f2b92314da012b9fffa36b3f3e67748a37ef464a
- https://github.com/pypa/pip
- https://lists.debian.org/debian-lts-announce/2025/10/msg00028.html
- https://mail.python.org/archives/list/security-announce@python.org/thread/IF5A3GCJY3VH7BVHJKOWOJFKTW7VFQEN
- https://pip.pypa.io/en/stable/news/#v25-2

