---
title: "GHSA-8qpc-6rxx-4pxf — PyPI vllm"
date: "2026-09-22"
layout: post
category: "advisory"
osv_id: "GHSA-8qpc-6rxx-4pxf"
ecosystem: "PyPI"
packages: ["vllm"]
cvss: 0
links: ["https://nvd.nist.gov/vuln/detail/CVE-2026-94624", "https://github.com/vllm-project/vllm/pull/51504", "https://github.com/pypa/advisory-database/tree/main/vulns/vllm/PYSEC-2026-4006.yaml", "https://github.com/vllm-project/vllm", "https://github.com/vllm-project/vllm/blob/v0.29.0/vllm/v1/kv_offload/tiering/p2p/control/zmq.py#L240-L260", "https://github.com/vllm-project/vllm/blob/v0.29.0/vllm/v1/kv_offload/tiering/p2p/manager.py#L667-L677", "https://www.vulncheck.com/advisories/vllm-through-0.29.0-denial-of-service-via-unbounded-p2p-kv-offloading-sessions"]
tags: ["pypi"]
---

Duplicate Advisory: vllm p2p never connected zmq_exhaustion

## References
- https://nvd.nist.gov/vuln/detail/CVE-2026-94624
- https://github.com/vllm-project/vllm/pull/51504
- https://github.com/pypa/advisory-database/tree/main/vulns/vllm/PYSEC-2026-4006.yaml
- https://github.com/vllm-project/vllm
- https://github.com/vllm-project/vllm/blob/v0.29.0/vllm/v1/kv_offload/tiering/p2p/control/zmq.py#L240-L260
- https://github.com/vllm-project/vllm/blob/v0.29.0/vllm/v1/kv_offload/tiering/p2p/manager.py#L667-L677
- https://www.vulncheck.com/advisories/vllm-through-0.29.0-denial-of-service-via-unbounded-p2p-kv-offloading-sessions

