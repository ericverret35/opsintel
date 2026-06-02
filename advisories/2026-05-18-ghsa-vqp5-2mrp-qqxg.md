---
title: "GHSA-vqp5-2mrp-qqxg — Go github.com/mattermost/mattermost/server/v8"
date: "2026-05-18"
layout: post
category: "advisory"
osv_id: "GHSA-vqp5-2mrp-qqxg"
ecosystem: "Go"
packages: ["github.com/mattermost/mattermost/server/v8", "github.com/mattermost/mattermost/server/v8", "github.com/mattermost/mattermost/server/v8", "github.com/mattermost/mattermost-server"]
cvss: 0
links: ["https://nvd.nist.gov/vuln/detail/CVE-2026-6333", "https://github.com/mattermost/mattermost/commit/e738016c592045e14bf926eafaeda6f8521def6d", "https://github.com/mattermost/mattermost", "https://mattermost.com/security-updates"]
tags: ["go"]
---

Mattermost doesn't validate the Host header when constructing response URLs for custom slash command

## References
- https://nvd.nist.gov/vuln/detail/CVE-2026-6333
- https://github.com/mattermost/mattermost/commit/e738016c592045e14bf926eafaeda6f8521def6d
- https://github.com/mattermost/mattermost
- https://mattermost.com/security-updates

