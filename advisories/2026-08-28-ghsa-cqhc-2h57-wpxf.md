---
title: "GHSA-cqhc-2h57-wpxf — npm mariadb"
date: "2026-08-28"
layout: post
category: "advisory"
osv_id: "GHSA-cqhc-2h57-wpxf"
ecosystem: "npm"
packages: ["mariadb", "mariadb", "mariadb", "mariadb"]
cvss: 0
links: ["https://github.com/mariadb-corporation/mariadb-connector-nodejs/security/advisories/GHSA-cqhc-2h57-wpxf", "https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/514576a5a1fab3ea8498613e259a0b7a764e7302", "https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/c47d7275835c78c7eb8186cd23e9d57c045c128b", "https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/ecd36958e6e3bf0e0fa8389546f50c0ed6dbb2ac", "https://hackerone.com/reports/3777370", "https://github.com/mariadb-corporation/mariadb-connector-nodejs", "https://github.com/mariadb-corporation/mariadb-connector-nodejs/releases/tag/3.3.3", "https://github.com/mariadb-corporation/mariadb-connector-nodejs/releases/tag/3.4.6", "https://github.com/mariadb-corporation/mariadb-connector-nodejs/releases/tag/3.5.3", "https://jira.mariadb.org/browse/CONJS-349"]
tags: ["npm"]
---

MariaDB's connector leaks the cleartext password to an MitM despite `ssl: true`

## References
- https://github.com/mariadb-corporation/mariadb-connector-nodejs/security/advisories/GHSA-cqhc-2h57-wpxf
- https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/514576a5a1fab3ea8498613e259a0b7a764e7302
- https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/c47d7275835c78c7eb8186cd23e9d57c045c128b
- https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/ecd36958e6e3bf0e0fa8389546f50c0ed6dbb2ac
- https://hackerone.com/reports/3777370
- https://github.com/mariadb-corporation/mariadb-connector-nodejs
- https://github.com/mariadb-corporation/mariadb-connector-nodejs/releases/tag/3.3.3
- https://github.com/mariadb-corporation/mariadb-connector-nodejs/releases/tag/3.4.6
- https://github.com/mariadb-corporation/mariadb-connector-nodejs/releases/tag/3.5.3
- https://jira.mariadb.org/browse/CONJS-349

