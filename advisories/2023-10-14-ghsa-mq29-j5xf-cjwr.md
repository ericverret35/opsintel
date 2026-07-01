---
title: "GHSA-mq29-j5xf-cjwr — PyPI pyminizip"
date: "2023-10-14"
layout: post
category: "advisory"
osv_id: "GHSA-mq29-j5xf-cjwr"
ecosystem: "PyPI"
packages: ["pyminizip"]
cvss: 0
links: ["https://nvd.nist.gov/vuln/detail/CVE-2023-45853", "https://github.com/madler/zlib/pull/843", "https://github.com/madler/zlib/commit/73331a6a0481067628f065ffe87bb1d8f787d10c", "https://chromium.googlesource.com/chromium/src/+/d709fb23806858847131027da95ef4c548813356", "https://chromium.googlesource.com/chromium/src/+/de29dd6c7151d3cd37cb4cf0036800ddfb1d8b61", "https://github.com/madler/zlib/blob/ac8f12c97d1afd9bafa9c710f827d40a407d3266/contrib/README.contrib#L1-L4", "https://github.com/smihica/pyminizip", "https://github.com/smihica/pyminizip/blob/master/zlib-1.2.11/contrib/minizip/zip.c", "https://lists.debian.org/debian-lts-announce/2023/11/msg00026.html", "https://pypi.org/project/pyminizip/#history", "https://security.gentoo.org/glsa/202401-18", "https://security.netapp.com/advisory/ntap-20231130-0009", "https://www.winimage.com/zLibDll/minizip.html", "http://www.openwall.com/lists/oss-security/2023/10/20/9", "http://www.openwall.com/lists/oss-security/2024/01/24/10"]
tags: ["pypi"]
---

pyminizip affected by zlib's integer overflow/heap based buffer overflow vulnerability due to vulnerable dependency

## References
- https://nvd.nist.gov/vuln/detail/CVE-2023-45853
- https://github.com/madler/zlib/pull/843
- https://github.com/madler/zlib/commit/73331a6a0481067628f065ffe87bb1d8f787d10c
- https://chromium.googlesource.com/chromium/src/+/d709fb23806858847131027da95ef4c548813356
- https://chromium.googlesource.com/chromium/src/+/de29dd6c7151d3cd37cb4cf0036800ddfb1d8b61
- https://github.com/madler/zlib/blob/ac8f12c97d1afd9bafa9c710f827d40a407d3266/contrib/README.contrib#L1-L4
- https://github.com/smihica/pyminizip
- https://github.com/smihica/pyminizip/blob/master/zlib-1.2.11/contrib/minizip/zip.c
- https://lists.debian.org/debian-lts-announce/2023/11/msg00026.html
- https://pypi.org/project/pyminizip/#history

