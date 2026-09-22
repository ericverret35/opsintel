---
title: "GHSA-f74p-cwhp-x2wx — Go github.com/grafana/grafana"
date: "2026-06-22"
layout: post
category: "advisory"
osv_id: "GHSA-f74p-cwhp-x2wx"
ecosystem: "Go"
packages: ["github.com/grafana/grafana", "github.com/grafana/grafana", "github.com/grafana/grafana", "github.com/grafana/grafana", "github.com/grafana/grafana", "github.com/grafana/grafana"]
cvss: 0
links: ["https://nvd.nist.gov/vuln/detail/CVE-2026-42129", "https://github.com/grafana/grafana/commit/3fcdbc5a6e5c955bd42bd3715dd03cbad2b078c1", "https://github.com/grafana/grafana/commit/42cdc39124912a8506a0c613c319c345aa950b29", "https://github.com/grafana/grafana/commit/82ef13993059351bf21de35b8488bbd9b42df4f4", "https://github.com/grafana/grafana/commit/d27d2eba9c509d16f214d290436a6ad0bd9c6c01", "https://github.com/grafana/grafana/commit/dd5dc51681ff0133ddb2e206c2ea318713aeca16", "https://github.com/grafana/grafana/commit/eeb08ceb020c4381242d8400e5878044e9877505", "https://github.com/grafana/grafana/commit/f70d3e480274a5dbd12006338c393f4b05d441ca", "https://github.com/grafana/grafana", "https://github.com/grafana/grafana/releases/tag/v11.6.15", "https://github.com/grafana/grafana/releases/tag/v12.2.9", "https://github.com/grafana/grafana/releases/tag/v12.3.7", "https://github.com/grafana/grafana/releases/tag/v12.4.4", "https://github.com/grafana/grafana/releases/tag/v13.0.2", "https://grafana.com/security/security-advisories/cve-2026-42129"]
tags: ["go"]
---

Grafana Loki datasource plugin's callResource handler contains a path traversal vulnerability.

## References
- https://nvd.nist.gov/vuln/detail/CVE-2026-42129
- https://github.com/grafana/grafana/commit/3fcdbc5a6e5c955bd42bd3715dd03cbad2b078c1
- https://github.com/grafana/grafana/commit/42cdc39124912a8506a0c613c319c345aa950b29
- https://github.com/grafana/grafana/commit/82ef13993059351bf21de35b8488bbd9b42df4f4
- https://github.com/grafana/grafana/commit/d27d2eba9c509d16f214d290436a6ad0bd9c6c01
- https://github.com/grafana/grafana/commit/dd5dc51681ff0133ddb2e206c2ea318713aeca16
- https://github.com/grafana/grafana/commit/eeb08ceb020c4381242d8400e5878044e9877505
- https://github.com/grafana/grafana/commit/f70d3e480274a5dbd12006338c393f4b05d441ca
- https://github.com/grafana/grafana
- https://github.com/grafana/grafana/releases/tag/v11.6.15

