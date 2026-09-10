---
title: "GHSA-5rjg-fvgr-3xxf — PyPI setuptools"
date: "2025-05-19"
layout: post
category: "advisory"
osv_id: "GHSA-5rjg-fvgr-3xxf"
ecosystem: "PyPI"
packages: ["setuptools"]
cvss: 0
links: ["https://github.com/pypa/setuptools/security/advisories/GHSA-5rjg-fvgr-3xxf", "https://nvd.nist.gov/vuln/detail/CVE-2025-47273", "https://github.com/pypa/setuptools/issues/4946", "https://github.com/pypa/setuptools/commit/250a6d17978f9f6ac3ac887091f2d32886fbbb0b", "https://github.com/pypa/advisory-database/tree/main/vulns/setuptools/PYSEC-2025-49.yaml", "https://github.com/pypa/setuptools", "https://github.com/pypa/setuptools/blob/6ead555c5fb29bc57fe6105b1bffc163f56fd558/setuptools/package_index.py#L810C1-L825C88", "https://lists.debian.org/debian-lts-announce/2025/05/msg00035.html"]
tags: ["pypi"]
---

setuptools has a path traversal vulnerability in PackageIndex.download that leads to Arbitrary File Write

## References
- https://github.com/pypa/setuptools/security/advisories/GHSA-5rjg-fvgr-3xxf
- https://nvd.nist.gov/vuln/detail/CVE-2025-47273
- https://github.com/pypa/setuptools/issues/4946
- https://github.com/pypa/setuptools/commit/250a6d17978f9f6ac3ac887091f2d32886fbbb0b
- https://github.com/pypa/advisory-database/tree/main/vulns/setuptools/PYSEC-2025-49.yaml
- https://github.com/pypa/setuptools
- https://github.com/pypa/setuptools/blob/6ead555c5fb29bc57fe6105b1bffc163f56fd558/setuptools/package_index.py#L810C1-L825C88
- https://lists.debian.org/debian-lts-announce/2025/05/msg00035.html

