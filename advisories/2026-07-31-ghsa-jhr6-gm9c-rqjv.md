---
title: "GHSA-jhr6-gm9c-rqjv — PyPI sentence-transformers"
date: "2026-07-31"
layout: post
category: "advisory"
osv_id: "GHSA-jhr6-gm9c-rqjv"
ecosystem: "PyPI"
packages: ["sentence-transformers"]
cvss: 0
links: ["https://nvd.nist.gov/vuln/detail/CVE-2026-68770", "https://github.com/huggingface/sentence-transformers/issues/3801", "https://github.com/huggingface/sentence-transformers/pull/3807", "https://github.com/huggingface/sentence-transformers/pull/3935", "https://github.com/huggingface/sentence-transformers/commit/626eb602b088878a8173bcab69225f68411b99e1", "https://github.com/huggingface/sentence-transformers/commit/ae1acc3fb2aa2004577b297eb4a915ce7a03316a", "https://github.com/huggingface/sentence-transformers", "https://github.com/huggingface/sentence-transformers/releases/tag/v5.6.0", "https://github.com/huggingface/sentence-transformers/releases/tag/v6.0.0", "https://www.vulncheck.com/advisories/sentence-transformers-arbitrary-code-execution-on-local-model-load-despite-trust-remote-code-false"]
tags: ["pypi"]
---

sentence-transformers local model loading bypasses trust_remote_code and executes custom Python

## References
- https://nvd.nist.gov/vuln/detail/CVE-2026-68770
- https://github.com/huggingface/sentence-transformers/issues/3801
- https://github.com/huggingface/sentence-transformers/pull/3807
- https://github.com/huggingface/sentence-transformers/pull/3935
- https://github.com/huggingface/sentence-transformers/commit/626eb602b088878a8173bcab69225f68411b99e1
- https://github.com/huggingface/sentence-transformers/commit/ae1acc3fb2aa2004577b297eb4a915ce7a03316a
- https://github.com/huggingface/sentence-transformers
- https://github.com/huggingface/sentence-transformers/releases/tag/v5.6.0
- https://github.com/huggingface/sentence-transformers/releases/tag/v6.0.0
- https://www.vulncheck.com/advisories/sentence-transformers-arbitrary-code-execution-on-local-model-load-despite-trust-remote-code-false

