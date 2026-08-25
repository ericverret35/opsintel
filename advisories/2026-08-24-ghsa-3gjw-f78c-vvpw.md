---
title: "GHSA-3gjw-f78c-vvpw — crates.io tokio-postgres"
date: "2026-08-24"
layout: post
category: "advisory"
osv_id: "GHSA-3gjw-f78c-vvpw"
ecosystem: "crates.io"
packages: ["tokio-postgres"]
cvss: 0
links: ["https://github.com/rust-postgres/rust-postgres/commit/7a00ffa9ad4d951ec0a4564b52f1780fa9d353c1", "https://github.com/rust-postgres/rust-postgres", "https://github.com/rust-postgres/rust-postgres/releases/tag/tokio-postgres-v0.7.18", "https://rustsec.org/advisories/RUSTSEC-2026-0178.html"]
tags: ["crates.io"]
---

tokio-postgres: Panic on a `DataRow` with fewer fields than columns allows denial of service

## References
- https://github.com/rust-postgres/rust-postgres/commit/7a00ffa9ad4d951ec0a4564b52f1780fa9d353c1
- https://github.com/rust-postgres/rust-postgres
- https://github.com/rust-postgres/rust-postgres/releases/tag/tokio-postgres-v0.7.18
- https://rustsec.org/advisories/RUSTSEC-2026-0178.html

