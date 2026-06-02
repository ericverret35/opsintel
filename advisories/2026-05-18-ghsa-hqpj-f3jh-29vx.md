---
title: "GHSA-hqpj-f3jh-29vx — Go github.com/mattermost/mattermost/server/v8"
date: "2026-05-18"
layout: post
category: "advisory"
osv_id: "GHSA-hqpj-f3jh-29vx"
ecosystem: "Go"
packages: ["github.com/mattermost/mattermost/server/v8", "github.com/mattermost/mattermost/server/v8", "github.com/mattermost/mattermost/server/v8", "github.com/mattermost/mattermost-server"]
cvss: 0
links: ["https://nvd.nist.gov/vuln/detail/CVE-2026-4273", "https://github.com/mattermost/mattermost/commit/742e0be9507454a7e662668e1d9ec1b94b636e9b", "https://github.com/mattermost/mattermost", "https://mattermost.com/security-updates"]
tags: ["go"]
---

Mattermost doesn't validate that the RefreshedToken differs from the original invite token during remote cluster invite confirmation

## References
- https://nvd.nist.gov/vuln/detail/CVE-2026-4273
- https://github.com/mattermost/mattermost/commit/742e0be9507454a7e662668e1d9ec1b94b636e9b
- https://github.com/mattermost/mattermost
- https://mattermost.com/security-updates

