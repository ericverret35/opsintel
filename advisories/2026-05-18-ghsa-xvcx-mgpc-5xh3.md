---
title: "GHSA-xvcx-mgpc-5xh3 — Go github.com/mattermost/mattermost/server/v8"
date: "2026-05-18"
layout: post
category: "advisory"
osv_id: "GHSA-xvcx-mgpc-5xh3"
ecosystem: "Go"
packages: ["github.com/mattermost/mattermost/server/v8", "github.com/mattermost/mattermost/server/v8", "github.com/mattermost/mattermost/server/v8", "github.com/mattermost/mattermost-server"]
cvss: 0
links: ["https://nvd.nist.gov/vuln/detail/CVE-2026-6339", "https://github.com/mattermost/mattermost/commit/7a339a6438f5a4a5feba6b8de887f17a1378b207", "https://github.com/mattermost/mattermost", "https://mattermost.com/security-updates"]
tags: ["go"]
---

Mattermost doesn't validate the X-Requested-With header on the burn-on-read reveal endpoint

## References
- https://nvd.nist.gov/vuln/detail/CVE-2026-6339
- https://github.com/mattermost/mattermost/commit/7a339a6438f5a4a5feba6b8de887f17a1378b207
- https://github.com/mattermost/mattermost
- https://mattermost.com/security-updates

