---
layout: post
title: 'Velero Backs Up to the Cluster It''s Backing Up: Breaking the Backup Circularity'
date: '2026-10-19'
category: tech-news
source: Dev.to
url: https://dev.to/dwoitzik/velero-backs-up-to-the-cluster-its-backing-up-breaking-the-backup-circularity-4f35
tags:
- tech-news
- dev.to
---

## Velero Backs Up to the Cluster It's Backing Up: Breaking the Backup Circularity

**Source**: Dev.to

 
  Originally published at  woitzik.dev   
 

  Disclosure: This post contains Amazon affiliate links (marked with *). If you buy through them, I earn a small commission at no extra cost to you. I only link gear I actually own and use daily.  

 The circularity:  Velero  backs up into Garage S3, which runs inside the Kubernetes cluster it's backing up. Cluster lost → Garage PVC lost → Velero backup bucket gone → nothing to restore from. 

 This is the backup equivalent of storing your offsite b

**Lien**: [Lire](https://dev.to/dwoitzik/velero-backs-up-to-the-cluster-its-backing-up-breaking-the-backup-circularity-4f35)
