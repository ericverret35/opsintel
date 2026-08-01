---
title: "GHSA-vccv-cmxp-4j9h — npm sanitize-html"
date: "2026-07-31"
layout: post
category: "advisory"
osv_id: "GHSA-vccv-cmxp-4j9h"
ecosystem: "npm"
packages: ["sanitize-html"]
cvss: 0
links: ["https://github.com/apostrophecms/apostrophe/security/advisories/GHSA-vccv-cmxp-4j9h", "https://nvd.nist.gov/vuln/detail/CVE-2026-53606", "https://github.com/apostrophecms/apostrophe/pull/5464", "https://github.com/apostrophecms/apostrophe/commit/5a88e9630cbbdde33154ef8abe7557ddf7be418b", "https://github.com/apostrophecms/apostrophe", "https://github.com/apostrophecms/apostrophe/releases/tag/sanitize-html@2.17.5"]
tags: ["npm"]
---

sanitize-html has incomplete URI scheme validation in that allows javascript: URIs through action, formaction, data, poster, and background attributes

## References
- https://github.com/apostrophecms/apostrophe/security/advisories/GHSA-vccv-cmxp-4j9h
- https://nvd.nist.gov/vuln/detail/CVE-2026-53606
- https://github.com/apostrophecms/apostrophe/pull/5464
- https://github.com/apostrophecms/apostrophe/commit/5a88e9630cbbdde33154ef8abe7557ddf7be418b
- https://github.com/apostrophecms/apostrophe
- https://github.com/apostrophecms/apostrophe/releases/tag/sanitize-html@2.17.5

