---
layout: post
title: A nightly pg_dump that fails with the reason, not with "Network is unreachable"
date: '2026-09-17'
category: tech-news
source: Dev.to
url: https://dev.to/daniel_pertu/a-nightly-pgdump-that-fails-with-the-reason-not-with-network-is-unreachable-4lg8
tags:
- tech-news
- dev.to
---

## A nightly pg_dump that fails with the reason, not with "Network is unreachable"

**Source**: Dev.to

  Munchable 's Postgres runs on a hosted tier that provides no managed backups. That makes a nightly GitHub Actions job the only line of defence against data loss, so the workflow is intentionally simple and loud:  pg_dump  to Cloudflare R2, and if it fails, the platform emails the repo admins. This post is about the checks that were added to it 27 minutes after it first shipped, and the ones that were there from the start. 

 
  
  
  Two archives, two retention windows
 



 
   #   full  ever

**Lien**: [Lire](https://dev.to/daniel_pertu/a-nightly-pgdump-that-fails-with-the-reason-not-with-network-is-unreachable-4lg8)
