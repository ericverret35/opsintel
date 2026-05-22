---
title: "GHSA-28xx-pppm-vqff — Go github.com/ydb-platform/ydb-go-sdk/v3"
date: "2026-04-30"
layout: post
category: "advisory"
osv_id: "GHSA-28xx-pppm-vqff"
ecosystem: "Go"
packages: ["github.com/ydb-platform/ydb-go-sdk/v3"]
cvss: 0
links: ["https://github.com/ydb-platform/ydb-go-sdk/security/advisories/GHSA-28xx-pppm-vqff", "https://github.com/ydb-platform/ydb-go-sdk/pull/2091", "https://github.com/ydb-platform/ydb-go-sdk/commit/251128a64763555d9a79ee7a131dd154c9000eb9", "https://github.com/ydb-platform/ydb-go-sdk/commit/25dcff4c41153f1f9413512ba12999b40bf7154d", "https://github.com/ydb-platform/ydb-go-sdk", "https://github.com/ydb-platform/ydb-go-sdk/releases/tag/v3.104.6", "https://github.com/ydb-platform/ydb-go-sdk/releases/tag/v3.134.1", "https://github.com/ydb-platform/ydb-go-sdk/releases/tag/v3.134.2"]
tags: ["go"]
---

ydb-go-sdk's transactions are not committed using the `options.WithCommit()` option on last call `table.Transaction.Execute` in transaction

## References
- https://github.com/ydb-platform/ydb-go-sdk/security/advisories/GHSA-28xx-pppm-vqff
- https://github.com/ydb-platform/ydb-go-sdk/pull/2091
- https://github.com/ydb-platform/ydb-go-sdk/commit/251128a64763555d9a79ee7a131dd154c9000eb9
- https://github.com/ydb-platform/ydb-go-sdk/commit/25dcff4c41153f1f9413512ba12999b40bf7154d
- https://github.com/ydb-platform/ydb-go-sdk
- https://github.com/ydb-platform/ydb-go-sdk/releases/tag/v3.104.6
- https://github.com/ydb-platform/ydb-go-sdk/releases/tag/v3.134.1
- https://github.com/ydb-platform/ydb-go-sdk/releases/tag/v3.134.2

