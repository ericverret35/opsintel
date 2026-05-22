---
title: "GHSA-36rr-ww3j-vrjv — PyPI keras"
date: "2025-09-19"
layout: post
category: "advisory"
osv_id: "GHSA-36rr-ww3j-vrjv"
ecosystem: "PyPI"
packages: ["keras"]
cvss: 0
links: ["https://github.com/keras-team/keras/security/advisories/GHSA-36rr-ww3j-vrjv", "https://nvd.nist.gov/vuln/detail/CVE-2025-9905", "https://github.com/keras-team/keras/pull/21602", "https://github.com/keras-team/keras"]
tags: ["pypi"]
---

The Keras `Model.load_model` method **silently** ignores `safe_mode=True` and allows arbitrary code execution when a `.h5`/`.hdf5` file is loaded.

## References
- https://github.com/keras-team/keras/security/advisories/GHSA-36rr-ww3j-vrjv
- https://nvd.nist.gov/vuln/detail/CVE-2025-9905
- https://github.com/keras-team/keras/pull/21602
- https://github.com/keras-team/keras

