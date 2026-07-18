---
title: "GHSA-chgr-c6px-7xpp — crates.io pyo3"
date: "2026-06-12"
layout: post
category: "advisory"
osv_id: "GHSA-chgr-c6px-7xpp"
ecosystem: "crates.io"
packages: ["pyo3"]
cvss: 0
links: ["https://github.com/PyO3/pyo3/pull/6096", "https://github.com/PyO3/pyo3", "https://github.com/PyO3/pyo3/releases/tag/v0.29.0", "https://rustsec.org/advisories/RUSTSEC-2026-0177.html"]
tags: ["crates.io"]
---

PyO3 has a missing `Sync` bound on `PyCFunction::new_closure` closures

## References
- https://github.com/PyO3/pyo3/pull/6096
- https://github.com/PyO3/pyo3
- https://github.com/PyO3/pyo3/releases/tag/v0.29.0
- https://rustsec.org/advisories/RUSTSEC-2026-0177.html

