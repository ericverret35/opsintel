---
title: "GHSA-vghh-5rfx-xhq8 — Go github.com/canonical/lxd"
date: "2026-11-06"
layout: post
category: "advisory"
osv_id: "GHSA-vghh-5rfx-xhq8"
ecosystem: "Go"
packages: ["github.com/canonical/lxd"]
cvss: 0
links: ["https://github.com/canonical/lxd/security/advisories/GHSA-vghh-5rfx-xhq8", "https://github.com/lxc/incus/security/advisories/GHSA-2q3f-q5pq-g8wv", "https://nvd.nist.gov/vuln/detail/CVE-2026-48749", "https://github.com/canonical/lxd/commit/190e2451544a60f6f924ef50a2112fb65d1923cd", "https://github.com/canonical/lxd/commit/254b85c9301397e25304116b63da9154093199da", "https://github.com/canonical/lxd/commit/3dbf4cea14124abda420dd5048d7e657cd30c1b7", "https://github.com/canonical/lxd/commit/4cd63344f8a523acf39fdc02a80fd64b2e3b584f", "https://github.com/canonical/lxd/commit/51dc11ed5258fbb54dd8993b802af02d6d7b0235", "https://github.com/canonical/lxd/commit/62bcee5471c2581fce10a648f6b27410ce081b87", "https://github.com/canonical/lxd/commit/8751ea69e24583996a20fb5519dcf2d89470d8e9", "https://github.com/canonical/lxd/commit/b499ec4b91dcc90f43aea444b1e19a58109772c2", "https://github.com/canonical/lxd/commit/e2aeca6b78677751bab36a7e4efaad0c840ed9fd", "https://github.com/canonical/lxd/commit/edb6d994f77333c9c33f4d9a137c754d142f3818", "https://github.com/canonical/lxd"]
tags: ["go"]
---

LXD has arbitrary file read+write on host via rootfs/ symlink in malicious image

## References
- https://github.com/canonical/lxd/security/advisories/GHSA-vghh-5rfx-xhq8
- https://github.com/lxc/incus/security/advisories/GHSA-2q3f-q5pq-g8wv
- https://nvd.nist.gov/vuln/detail/CVE-2026-48749
- https://github.com/canonical/lxd/commit/190e2451544a60f6f924ef50a2112fb65d1923cd
- https://github.com/canonical/lxd/commit/254b85c9301397e25304116b63da9154093199da
- https://github.com/canonical/lxd/commit/3dbf4cea14124abda420dd5048d7e657cd30c1b7
- https://github.com/canonical/lxd/commit/4cd63344f8a523acf39fdc02a80fd64b2e3b584f
- https://github.com/canonical/lxd/commit/51dc11ed5258fbb54dd8993b802af02d6d7b0235
- https://github.com/canonical/lxd/commit/62bcee5471c2581fce10a648f6b27410ce081b87
- https://github.com/canonical/lxd/commit/8751ea69e24583996a20fb5519dcf2d89470d8e9

