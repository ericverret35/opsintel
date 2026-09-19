---
title: "GHSA-c8w2-fgvx-vhv4 — Go github.com/kcp-dev/kcp"
date: "2026-09-18"
layout: post
category: "advisory"
osv_id: "GHSA-c8w2-fgvx-vhv4"
ecosystem: "Go"
packages: ["github.com/kcp-dev/kcp", "github.com/kcp-dev/kcp"]
cvss: 0
links: ["https://github.com/kcp-dev/kcp/security/advisories/GHSA-c8w2-fgvx-vhv4", "https://github.com/kcp-dev/kcp/commit/7437cdcfec8f927d1a9bf1b2dd1e075d038e27ca", "https://github.com/kcp-dev/kcp", "https://github.com/kcp-dev/kcp/releases/tag/v0.31.4", "https://github.com/kcp-dev/kcp/releases/tag/v0.32.2"]
tags: ["go"]
---

kcp front-proxy does not strip inbound X-Remote-* identity headers, allowing any authenticated client to inject groups/warrants and impersonate system:masters in any workspace

## References
- https://github.com/kcp-dev/kcp/security/advisories/GHSA-c8w2-fgvx-vhv4
- https://github.com/kcp-dev/kcp/commit/7437cdcfec8f927d1a9bf1b2dd1e075d038e27ca
- https://github.com/kcp-dev/kcp
- https://github.com/kcp-dev/kcp/releases/tag/v0.31.4
- https://github.com/kcp-dev/kcp/releases/tag/v0.32.2

