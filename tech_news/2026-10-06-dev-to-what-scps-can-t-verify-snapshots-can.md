---
layout: post
title: What SCPs Can't Verify, Snapshots Can
date: '2026-10-06'
category: tech-news
source: Dev.to
url: https://dev.to/bala_paranj_059d338e44e7e/what-scps-cant-verify-snapshots-can-3668
tags:
- tech-news
- dev.to
---

## What SCPs Can't Verify, Snapshots Can

**Source**: Dev.to

 
 ✓ Human-authored analysis; AI used for formatting and proofreading. 
 

 Can an SCP require EKS clusters to use customer-managed KMS keys? 

 No. Because the information the SCP needs doesn't exist in the place the SCP can look. 

 
  
  
  The request context is incomplete
 

 What happens when someone creates an EKS cluster with encryption: 
 

 
  aws eks create-cluster  \ 
   --name  production  \ 
   --encryption-config   '[{
    "provider": {
      "keyArn": "arn:aws:kms:us-east-1:12345

**Lien**: [Lire](https://dev.to/bala_paranj_059d338e44e7e/what-scps-cant-verify-snapshots-can-3668)
