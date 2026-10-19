---
layout: post
title: 'Capability-scoped reports: SAST, deps, images, secrets, licenses'
date: '2026-10-19'
category: tech-news
source: Dev.to
url: https://dev.to/wenping/capability-scoped-reports-sast-deps-images-secrets-licenses-i9
tags:
- tech-news
- dev.to
---

## Capability-scoped reports: SAST, deps, images, secrets, licenses

**Source**: Dev.to

 A full-capability report is too thick: engineers want code paths, supply-chain wants CVEs, compliance wants license exceptions—do not invent five unrelated exporters. Narrow filters on the  same report snapshot . 

 
  Takeaway:  First follow the report-export article to pick an audience and freeze a READY snapshot; then filter by capability/engine:  sast  (OpenGrep),  sca  (Trivy: deps/artifacts/images),  secret  (Gitleaks), and license-related filters. SARIF only covers finding details (SAST/

**Lien**: [Lire](https://dev.to/wenping/capability-scoped-reports-sast-deps-images-secrets-licenses-i9)
