---
title: "GHSA-9jhj-wvmw-cfx5 — npm i18next-http-backend"
date: "2026-10-28"
layout: post
category: "advisory"
osv_id: "GHSA-9jhj-wvmw-cfx5"
ecosystem: "npm"
packages: ["i18next-http-backend"]
cvss: 0
links: ["https://github.com/i18next/i18next-http-backend/security/advisories/GHSA-9jhj-wvmw-cfx5", "https://nvd.nist.gov/vuln/detail/CVE-2026-115730", "https://github.com/i18next/i18next-http-backend/commit/042c3d4e4e9d73b2ae3aa76b22cb45d48f1e35b7", "https://github.com/i18next/i18next-http-backend", "https://www.vulncheck.com/advisories/i18next-http-backend-4.0.2-protocol-relative-url-injection-via-namespace-in-interpolateurl"]
tags: ["npm"]
---

i18next-http-backend: Namespace value starting with / forms a protocol-relative URL when loadPath/addPath places {{ns}} right after a / (bypass of the // check added for GHSA-xvq9-wjp8-hwqf)

## References
- https://github.com/i18next/i18next-http-backend/security/advisories/GHSA-9jhj-wvmw-cfx5
- https://nvd.nist.gov/vuln/detail/CVE-2026-115730
- https://github.com/i18next/i18next-http-backend/commit/042c3d4e4e9d73b2ae3aa76b22cb45d48f1e35b7
- https://github.com/i18next/i18next-http-backend
- https://www.vulncheck.com/advisories/i18next-http-backend-4.0.2-protocol-relative-url-injection-via-namespace-in-interpolateurl

