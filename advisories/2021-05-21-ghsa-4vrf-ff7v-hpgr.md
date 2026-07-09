---
title: "GHSA-4vrf-ff7v-hpgr — PyPI tensorflow"
date: "2021-05-21"
layout: post
category: "advisory"
osv_id: "GHSA-4vrf-ff7v-hpgr"
ecosystem: "PyPI"
packages: ["tensorflow", "tensorflow", "tensorflow", "tensorflow", "tensorflow-cpu", "tensorflow-cpu", "tensorflow-cpu", "tensorflow-cpu", "tensorflow-gpu", "tensorflow-gpu", "tensorflow-gpu", "tensorflow-gpu"]
cvss: 0
links: ["https://github.com/tensorflow/tensorflow/security/advisories/GHSA-4vrf-ff7v-hpgr", "https://nvd.nist.gov/vuln/detail/CVE-2021-29596", "https://github.com/tensorflow/tensorflow/commit/f61c57bd425878be108ec787f4d96390579fb83e", "https://github.com/pypa/advisory-database/tree/main/vulns/tensorflow-cpu/PYSEC-2021-524.yaml", "https://github.com/pypa/advisory-database/tree/main/vulns/tensorflow-gpu/PYSEC-2021-722.yaml", "https://github.com/pypa/advisory-database/tree/main/vulns/tensorflow/PYSEC-2021-233.yaml", "https://github.com/tensorflow/tensorflow", "https://github.com/tensorflow/tensorflow/blob/e4b29809543b250bc9b19678ec4776299dd569ba/tensorflow/lite/kernels/embedding_lookup.cc#L73-L74"]
tags: ["pypi"]
---

Division by zero in TFLite's implementation of `EmbeddingLookup`

## References
- https://github.com/tensorflow/tensorflow/security/advisories/GHSA-4vrf-ff7v-hpgr
- https://nvd.nist.gov/vuln/detail/CVE-2021-29596
- https://github.com/tensorflow/tensorflow/commit/f61c57bd425878be108ec787f4d96390579fb83e
- https://github.com/pypa/advisory-database/tree/main/vulns/tensorflow-cpu/PYSEC-2021-524.yaml
- https://github.com/pypa/advisory-database/tree/main/vulns/tensorflow-gpu/PYSEC-2021-722.yaml
- https://github.com/pypa/advisory-database/tree/main/vulns/tensorflow/PYSEC-2021-233.yaml
- https://github.com/tensorflow/tensorflow
- https://github.com/tensorflow/tensorflow/blob/e4b29809543b250bc9b19678ec4776299dd569ba/tensorflow/lite/kernels/embedding_lookup.cc#L73-L74

