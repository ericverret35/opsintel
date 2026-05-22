---
title: "GHSA-fh64-r2vc-xvhr — PyPI mlflow"
date: "2026-04-07"
layout: post
category: "advisory"
osv_id: "GHSA-fh64-r2vc-xvhr"
ecosystem: "PyPI"
packages: ["mlflow"]
cvss: 0
links: ["https://nvd.nist.gov/vuln/detail/CVE-2026-33865", "https://github.com/mlflow/mlflow/pull/21435", "https://github.com/mlflow/mlflow/commit/aca4dd0ec88a12f7655155c224371280e9b45dda", "https://afine.com/blogs/attacking-mlflow-how-ml-artifacts-become-attack-vectors", "https://cert.pl/en/posts/2026/04/CVE-2026-33865", "https://github.com/mlflow/mlflow"]
tags: ["pypi"]
---

MLflow is vulnerable to Stored Cross-Site Scripting (XSS) caused by unsafe parsing of YAML-based MLmodel artifacts in its web interface

## References
- https://nvd.nist.gov/vuln/detail/CVE-2026-33865
- https://github.com/mlflow/mlflow/pull/21435
- https://github.com/mlflow/mlflow/commit/aca4dd0ec88a12f7655155c224371280e9b45dda
- https://afine.com/blogs/attacking-mlflow-how-ml-artifacts-become-attack-vectors
- https://cert.pl/en/posts/2026/04/CVE-2026-33865
- https://github.com/mlflow/mlflow

