---
layout: post
title: 'Updating the vuln DB on an intranet: offline bundles and rollback'
date: '2026-10-19'
category: tech-news
source: Dev.to
url: https://dev.to/wenping/updating-the-vuln-db-on-an-intranet-offline-bundles-and-rollback-294k
tags:
- tech-news
- dev.to
---

## Updating the vuln DB on an intranet: offline bundles and rollback

**Source**: Dev.to

 Intranet CI keeps returning  PASSED  on an image while the same image on the public network shows a pile of CRITICAL findings—do not loosen  --fail-on  first. Check whether the  Trivy vulnerability DB  is months stale, or whether an offline import left you pointing at an empty or half-written cache. 

 
  Takeaway:  SCA (software composition analysis) reads Trivy’s local vulnerability DB. On networked hosts run  update-trivy-db.sh . On air-gapped hosts import an offline bundle or land a manuall

**Lien**: [Lire](https://dev.to/wenping/updating-the-vuln-db-on-an-intranet-offline-bundles-and-rollback-294k)
