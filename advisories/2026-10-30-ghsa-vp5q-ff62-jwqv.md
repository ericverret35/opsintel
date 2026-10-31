---
title: "GHSA-vp5q-ff62-jwqv — crates.io russh"
date: "2026-10-30"
layout: post
category: "advisory"
osv_id: "GHSA-vp5q-ff62-jwqv"
ecosystem: "crates.io"
packages: ["russh"]
cvss: 0
links: ["https://github.com/Eugeny/russh/security/advisories/GHSA-vp5q-ff62-jwqv", "https://nvd.nist.gov/vuln/detail/CVE-2026-116794", "https://github.com/Eugeny/russh/commit/3e04597dc54e36bfc85c21996f7d8d9d224e9826", "https://github.com/Eugeny/russh/commit/62db6e7defd6d244159da962ccccb029e785ce0f", "https://github.com/Eugeny/russh", "https://github.com/Eugeny/russh/releases/tag/v0.65.0"]
tags: ["crates.io"]
---

russh: Agent server never calls `Agent::confirm`, so keys added with the confirm constraint (`ssh-add -c`) sign without confirmation

## References
- https://github.com/Eugeny/russh/security/advisories/GHSA-vp5q-ff62-jwqv
- https://nvd.nist.gov/vuln/detail/CVE-2026-116794
- https://github.com/Eugeny/russh/commit/3e04597dc54e36bfc85c21996f7d8d9d224e9826
- https://github.com/Eugeny/russh/commit/62db6e7defd6d244159da962ccccb029e785ce0f
- https://github.com/Eugeny/russh
- https://github.com/Eugeny/russh/releases/tag/v0.65.0

