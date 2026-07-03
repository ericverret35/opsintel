---
title: "GHSA-whqr-fgm5-x77q — PyPI keystone"
date: "2026-05-28"
layout: post
category: "advisory"
osv_id: "GHSA-whqr-fgm5-x77q"
ecosystem: "PyPI"
packages: ["keystone", "keystone", "keystone"]
cvss: 0
links: ["https://nvd.nist.gov/vuln/detail/CVE-2026-44394", "https://bugs.launchpad.net/keystone/+bug/2150379", "https://github.com/openstack/keystone", "https://github.com/pypa/advisory-database/tree/main/vulns/keystone/PYSEC-2026-603.yaml", "https://security.openstack.org/ossa/OSSA-2026-015.html"]
tags: ["pypi"]
---

OpenStack Keystone's federated token rescoping mechanism doesn't propagate the original token's expiry to the newly issued token

## References
- https://nvd.nist.gov/vuln/detail/CVE-2026-44394
- https://bugs.launchpad.net/keystone/+bug/2150379
- https://github.com/openstack/keystone
- https://github.com/pypa/advisory-database/tree/main/vulns/keystone/PYSEC-2026-603.yaml
- https://security.openstack.org/ossa/OSSA-2026-015.html

