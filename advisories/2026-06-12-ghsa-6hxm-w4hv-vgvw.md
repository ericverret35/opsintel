---
title: "GHSA-6hxm-w4hv-vgvw — Go github.com/mattermost/mattermost-server"
date: "2026-06-12"
layout: post
category: "advisory"
osv_id: "GHSA-6hxm-w4hv-vgvw"
ecosystem: "Go"
packages: ["github.com/mattermost/mattermost-server", "github.com/mattermost/mattermost-server", "github.com/mattermost/mattermost-server", "github.com/mattermost/mattermost/server/v8"]
cvss: 0
links: ["https://nvd.nist.gov/vuln/detail/CVE-2026-7387", "https://github.com/mattermost/mattermost/pull/36434", "https://github.com/mattermost/mattermost/pull/36432", "https://github.com/mattermost/mattermost/pull/36431", "https://github.com/mattermost/mattermost/pull/36423", "https://github.com/mattermost/mattermost/pull/36316", "https://github.com/mattermost/mattermost/commit/d5f29c8ebbeb04460d16d9e2635ce50deeb78428", "https://github.com/mattermost/mattermost/commit/a9e574a82633915f22071f0d7ca2b006f249ec2a", "https://github.com/mattermost/mattermost/commit/8c72083414e675c97987374395e36d1f36b4bd8a", "https://github.com/mattermost/mattermost/commit/202d125afa87fe39611686850fd82590c99ca344", "https://github.com/mattermost/mattermost/commit/1ce2484a00c9821ee19708d2c46720e4855033a9", "https://github.com/mattermost/mattermost/releases/tag/v10.11.16", "https://github.com/mattermost/mattermost/releases/tag/v11.5.5", "https://github.com/mattermost/mattermost/releases/tag/v11.6.2", "https://github.com/mattermost/mattermost/releases/tag/v11.7.0", "https://mattermost.com/security-updates", "https://github.com/mattermost/mattermost"]
tags: ["go"]
---

Mattermost doesn't require role-management authorization when setting the scheme_admin flag on group syncable link and patch endpoints

## References
- https://nvd.nist.gov/vuln/detail/CVE-2026-7387
- https://github.com/mattermost/mattermost/pull/36434
- https://github.com/mattermost/mattermost/pull/36432
- https://github.com/mattermost/mattermost/pull/36431
- https://github.com/mattermost/mattermost/pull/36423
- https://github.com/mattermost/mattermost/pull/36316
- https://github.com/mattermost/mattermost/commit/d5f29c8ebbeb04460d16d9e2635ce50deeb78428
- https://github.com/mattermost/mattermost/commit/a9e574a82633915f22071f0d7ca2b006f249ec2a
- https://github.com/mattermost/mattermost/commit/8c72083414e675c97987374395e36d1f36b4bd8a
- https://github.com/mattermost/mattermost/commit/202d125afa87fe39611686850fd82590c99ca344

