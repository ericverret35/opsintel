---
title: "GHSA-hwvp-7xqv-8jx3 — Maven org.jenkins-ci.tools:git-parameter"
date: "2026-06-24"
layout: post
category: "advisory"
osv_id: "GHSA-hwvp-7xqv-8jx3"
ecosystem: "Maven"
packages: ["org.jenkins-ci.tools:git-parameter"]
cvss: 0
links: ["https://nvd.nist.gov/vuln/detail/CVE-2026-57286", "https://github.com/jenkinsci/git-parameter-plugin/commit/496a59f698e5ada712dea1ebf980709f0040e394", "https://github.com/jenkinsci/git-parameter-plugin", "https://github.com/jenkinsci/git-parameter-plugin/releases/tag/462.463.v496a_59f698e5", "https://www.jenkins.io/security/advisory/2026-06-24/#SECURITY-3745"]
tags: ["maven"]
---

Jenkins Git Parameter Plugin has a missing permission check that allows listing SCM branch and tag names

## References
- https://nvd.nist.gov/vuln/detail/CVE-2026-57286
- https://github.com/jenkinsci/git-parameter-plugin/commit/496a59f698e5ada712dea1ebf980709f0040e394
- https://github.com/jenkinsci/git-parameter-plugin
- https://github.com/jenkinsci/git-parameter-plugin/releases/tag/462.463.v496a_59f698e5
- https://www.jenkins.io/security/advisory/2026-06-24/#SECURITY-3745

