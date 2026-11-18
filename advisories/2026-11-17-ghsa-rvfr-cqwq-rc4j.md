---
title: "GHSA-rvfr-cqwq-rc4j — npm @libp2p/crypto"
date: "2026-11-17"
layout: post
category: "advisory"
osv_id: "GHSA-rvfr-cqwq-rc4j"
ecosystem: "npm"
packages: ["@libp2p/crypto"]
cvss: 0
links: ["https://github.com/libp2p/js-libp2p/security/advisories/GHSA-rvfr-cqwq-rc4j", "https://github.com/libp2p/js-libp2p/pull/3587", "https://github.com/libp2p/js-libp2p/commit/ef6e1851cb00511a4793a5e68948e0cdad385332", "https://github.com/libp2p/js-libp2p", "https://github.com/libp2p/js-libp2p/releases/tag/crypto-v5.1.22"]
tags: ["npm"]
---

libp2p: ASN.1 DER decoder drives an unbounded synchronous loop on attacker-controlled length fields, stalling the Node event loop pre-auth

## References
- https://github.com/libp2p/js-libp2p/security/advisories/GHSA-rvfr-cqwq-rc4j
- https://github.com/libp2p/js-libp2p/pull/3587
- https://github.com/libp2p/js-libp2p/commit/ef6e1851cb00511a4793a5e68948e0cdad385332
- https://github.com/libp2p/js-libp2p
- https://github.com/libp2p/js-libp2p/releases/tag/crypto-v5.1.22

