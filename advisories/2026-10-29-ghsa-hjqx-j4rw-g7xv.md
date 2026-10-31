---
title: "GHSA-hjqx-j4rw-g7xv — crates.io zip"
date: "2026-10-29"
layout: post
category: "advisory"
osv_id: "GHSA-hjqx-j4rw-g7xv"
ecosystem: "crates.io"
packages: ["zip"]
cvss: 0
links: ["https://github.com/zip-rs/zip2/security/advisories/GHSA-hjqx-j4rw-g7xv", "https://nvd.nist.gov/vuln/detail/CVE-2026-115908", "https://github.com/zip-rs/zip2/commit/09c030eab56e8db8fb3c1c33f554407b30bad8fa", "https://github.com/zip-rs/zip2", "https://github.com/zip-rs/zip2/releases/tag/v9.0.0"]
tags: ["crates.io"]
---

zip: Arbitrary file write outside the extraction directory, because ZipArchive::extract validates symlink targets lexically.

## References
- https://github.com/zip-rs/zip2/security/advisories/GHSA-hjqx-j4rw-g7xv
- https://nvd.nist.gov/vuln/detail/CVE-2026-115908
- https://github.com/zip-rs/zip2/commit/09c030eab56e8db8fb3c1c33f554407b30bad8fa
- https://github.com/zip-rs/zip2
- https://github.com/zip-rs/zip2/releases/tag/v9.0.0

