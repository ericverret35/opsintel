---
title: "GHSA-3vmp-whvv-5v9v — Go github.com/mattermost/mattermost-server"
date: "2026-06-12"
layout: post
category: "advisory"
osv_id: "GHSA-3vmp-whvv-5v9v"
ecosystem: "Go"
packages: ["github.com/mattermost/mattermost-server", "github.com/mattermost/mattermost-server", "github.com/mattermost/mattermost-server", "github.com/mattermost/mattermost/server/v8"]
cvss: 0
links: ["https://nvd.nist.gov/vuln/detail/CVE-2026-6046", "https://github.com/mattermost/mattermost/pull/36320", "https://github.com/mattermost/mattermost/pull/36318", "https://github.com/mattermost/mattermost/pull/36317", "https://github.com/mattermost/mattermost/pull/36305", "https://github.com/mattermost/mattermost/pull/36064", "https://github.com/mattermost/mattermost/commit/f706d1f01e6dfe62cab86c1d257f237daa78106a", "https://github.com/mattermost/mattermost/commit/c79c3831061a0880c0962c7d567c9e24dd35f44c", "https://github.com/mattermost/mattermost/commit/aba9339a24d4b287edd77377c19901d6e341bb96", "https://github.com/mattermost/mattermost/commit/98f9778cec1e7f3d97b3d4692fb91f8e7b659972", "https://github.com/mattermost/mattermost/commit/3be10297c14d272f273d747af70728f9d03c60ec", "https://github.com/mattermost/mattermost/releases/tag/v10.11.16", "https://github.com/mattermost/mattermost/releases/tag/v11.5.5", "https://github.com/mattermost/mattermost/releases/tag/v11.6.2", "https://github.com/mattermost/mattermost/releases/tag/v11.7.0", "https://mattermost.com/security-updates", "https://github.com/mattermost/mattermost"]
tags: ["go"]
---

Mattermost doesn't validate that a username returned during bot registration belongs to a bot account

## References
- https://nvd.nist.gov/vuln/detail/CVE-2026-6046
- https://github.com/mattermost/mattermost/pull/36320
- https://github.com/mattermost/mattermost/pull/36318
- https://github.com/mattermost/mattermost/pull/36317
- https://github.com/mattermost/mattermost/pull/36305
- https://github.com/mattermost/mattermost/pull/36064
- https://github.com/mattermost/mattermost/commit/f706d1f01e6dfe62cab86c1d257f237daa78106a
- https://github.com/mattermost/mattermost/commit/c79c3831061a0880c0962c7d567c9e24dd35f44c
- https://github.com/mattermost/mattermost/commit/aba9339a24d4b287edd77377c19901d6e341bb96
- https://github.com/mattermost/mattermost/commit/98f9778cec1e7f3d97b3d4692fb91f8e7b659972

