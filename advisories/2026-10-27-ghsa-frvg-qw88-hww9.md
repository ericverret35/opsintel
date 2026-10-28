---
title: "GHSA-frvg-qw88-hww9 — PyPI vllm"
date: "2026-10-27"
layout: post
category: "advisory"
osv_id: "GHSA-frvg-qw88-hww9"
ecosystem: "PyPI"
packages: ["vllm"]
cvss: 0
links: ["https://github.com/vllm-project/vllm/security/advisories/GHSA-frvg-qw88-hww9", "https://nvd.nist.gov/vuln/detail/CVE-2026-94624", "https://github.com/vllm-project/vllm/pull/51504", "https://github.com/vllm-project/vllm/commit/93d2cab35e8ae66bbaa1dea1c077986d5a79eb80", "https://github.com/pypa/advisory-database/tree/main/vulns/vllm/PYSEC-2026-4006.yaml", "https://github.com/vllm-project/vllm", "https://github.com/vllm-project/vllm/blob/v0.29.0/vllm/v1/kv_offload/tiering/p2p/control/zmq.py#L240-L260", "https://github.com/vllm-project/vllm/blob/v0.29.0/vllm/v1/kv_offload/tiering/p2p/manager.py#L667-L677", "https://github.com/vllm-project/vllm/releases/tag/v0.32.0", "https://www.vulncheck.com/advisories/vllm-through-0.29.0-denial-of-service-via-unbounded-p2p-kv-offloading-sessions"]
tags: ["pypi"]
---

vllm p2p never connected zmq_exhaustion

## References
- https://github.com/vllm-project/vllm/security/advisories/GHSA-frvg-qw88-hww9
- https://nvd.nist.gov/vuln/detail/CVE-2026-94624
- https://github.com/vllm-project/vllm/pull/51504
- https://github.com/vllm-project/vllm/commit/93d2cab35e8ae66bbaa1dea1c077986d5a79eb80
- https://github.com/pypa/advisory-database/tree/main/vulns/vllm/PYSEC-2026-4006.yaml
- https://github.com/vllm-project/vllm
- https://github.com/vllm-project/vllm/blob/v0.29.0/vllm/v1/kv_offload/tiering/p2p/control/zmq.py#L240-L260
- https://github.com/vllm-project/vllm/blob/v0.29.0/vllm/v1/kv_offload/tiering/p2p/manager.py#L667-L677
- https://github.com/vllm-project/vllm/releases/tag/v0.32.0
- https://www.vulncheck.com/advisories/vllm-through-0.29.0-denial-of-service-via-unbounded-p2p-kv-offloading-sessions

