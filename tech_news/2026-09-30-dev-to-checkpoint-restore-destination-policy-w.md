---
layout: post
title: 'Checkpoint Restore: Destination Policy Was Never Reapplied'
date: '2026-09-30'
category: tech-news
source: Dev.to
url: https://dev.to/ntctech/checkpoint-restore-destination-policy-was-never-reapplied-khd
tags:
- tech-news
- dev.to
---

## Checkpoint Restore: Destination Policy Was Never Reapplied

**Source**: Dev.to

 A checkpoint restore can rebuild a process from saved state without passing that state back through the destination's normal policy translation. When it does, the security context on the Pod spec describes the workload that was approved, and the process on the node is the one that was saved. 

 That is a boundary problem before it is a vulnerability problem. Kubernetes has one place where policy becomes process state, and it is creation. Restore is a second route to a running process, and nothi

**Lien**: [Lire](https://dev.to/ntctech/checkpoint-restore-destination-policy-was-never-reapplied-khd)
