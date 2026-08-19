---
title: "GHSA-wcwg-c5fc-9vrc — PyPI vllm"
date: "2026-06-11"
layout: post
category: "advisory"
osv_id: "GHSA-wcwg-c5fc-9vrc"
ecosystem: "PyPI"
packages: ["vllm"]
cvss: 0
links: ["https://nvd.nist.gov/vuln/detail/CVE-2026-5497", "https://github.com/vllm-project/vllm/commit/58ee61422169ce17e08248f8efa1e9df434fe395", "https://access.redhat.com/errata/RHSA-2026:33524", "https://access.redhat.com/errata/RHSA-2026:33531", "https://access.redhat.com/security/cve/CVE-2026-5497", "https://bugzilla.redhat.com/show_bug.cgi?id=2487813", "https://github.com/pypa/advisory-database/tree/main/vulns/vllm/PYSEC-2026-2302.yaml", "https://github.com/vllm-project/vllm", "https://huntr.com/bounties/7bd92629-b396-4449-8f88-6c0092530eb4", "https://security.access.redhat.com/data/csaf/v2/vex/2026/cve-2026-5497.json"]
tags: ["pypi"]
---

vLLM is vulnerable to an Out-of-Memory (OOM) Denial of Service (DoS) attack due to unbounded frame count processing in the `VideoMediaIO.load_base64()` method

## References
- https://nvd.nist.gov/vuln/detail/CVE-2026-5497
- https://github.com/vllm-project/vllm/commit/58ee61422169ce17e08248f8efa1e9df434fe395
- https://access.redhat.com/errata/RHSA-2026:33524
- https://access.redhat.com/errata/RHSA-2026:33531
- https://access.redhat.com/security/cve/CVE-2026-5497
- https://bugzilla.redhat.com/show_bug.cgi?id=2487813
- https://github.com/pypa/advisory-database/tree/main/vulns/vllm/PYSEC-2026-2302.yaml
- https://github.com/vllm-project/vllm
- https://huntr.com/bounties/7bd92629-b396-4449-8f88-6c0092530eb4
- https://security.access.redhat.com/data/csaf/v2/vex/2026/cve-2026-5497.json

