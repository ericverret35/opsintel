---
title: "GHSA-8mcc-hrx5-hvxc — PyPI gitpython"
date: "2026-09-08"
layout: post
category: "advisory"
osv_id: "GHSA-8mcc-hrx5-hvxc"
ecosystem: "PyPI"
packages: ["gitpython"]
cvss: 0
links: ["https://github.com/gitpython-developers/GitPython/security/advisories/GHSA-8mcc-hrx5-hvxc", "https://nvd.nist.gov/vuln/detail/CVE-2026-78677", "https://github.com/gitpython-developers/GitPython/pull/2210", "https://github.com/gitpython-developers/GitPython/commit/b68afff45af0f49e79a3e2d2162018986b37ad5d", "https://github.com/gitpython-developers/GitPython", "https://github.com/gitpython-developers/GitPython/releases/tag/3.1.59", "https://github.com/pypa/advisory-database/tree/main/vulns/gitpython/PYSEC-2026-3787.yaml", "https://www.vulncheck.com/advisories/gitpython-before-path-traversal-via-separate-git-dir"]
tags: ["pypi"]
---

GitPython: clone_from()/clone() omit --separate-git-dir from unsafe_git_clone_options, enabling arbitrary git-directory creation outside the destination

## References
- https://github.com/gitpython-developers/GitPython/security/advisories/GHSA-8mcc-hrx5-hvxc
- https://nvd.nist.gov/vuln/detail/CVE-2026-78677
- https://github.com/gitpython-developers/GitPython/pull/2210
- https://github.com/gitpython-developers/GitPython/commit/b68afff45af0f49e79a3e2d2162018986b37ad5d
- https://github.com/gitpython-developers/GitPython
- https://github.com/gitpython-developers/GitPython/releases/tag/3.1.59
- https://github.com/pypa/advisory-database/tree/main/vulns/gitpython/PYSEC-2026-3787.yaml
- https://www.vulncheck.com/advisories/gitpython-before-path-traversal-via-separate-git-dir

