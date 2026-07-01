---
title: "GHSA-pgr7-mhp5-fgjp — PyPI vllm"
date: "2025-03-20"
layout: post
category: "advisory"
osv_id: "GHSA-pgr7-mhp5-fgjp"
ecosystem: "PyPI"
packages: ["vllm"]
cvss: 0
links: ["https://nvd.nist.gov/vuln/detail/CVE-2024-9052", "https://github.com/github/advisory-database/pull/5444", "https://github.com/vllm-project/vllm", "https://github.com/vllm-project/vllm/blob/32e7db25365415841ebc7c4215851743fbb1bad1/vllm/distributed/parallel_state.py#L480", "https://github.com/vllm-project/vllm/blob/v0.8.1/vllm/distributed/parallel_state.py#L457", "https://huntr.com/bounties/ea75728f-4efe-4a3d-9f53-33f2c908e9f8"]
tags: ["pypi"]
---

vLLM deserialization vulnerability in vllm.distributed.GroupCoordinator.recv_object

## References
- https://nvd.nist.gov/vuln/detail/CVE-2024-9052
- https://github.com/github/advisory-database/pull/5444
- https://github.com/vllm-project/vllm
- https://github.com/vllm-project/vllm/blob/32e7db25365415841ebc7c4215851743fbb1bad1/vllm/distributed/parallel_state.py#L480
- https://github.com/vllm-project/vllm/blob/v0.8.1/vllm/distributed/parallel_state.py#L457
- https://huntr.com/bounties/ea75728f-4efe-4a3d-9f53-33f2c908e9f8

