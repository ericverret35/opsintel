---
layout: post
title: The .gitleaks-baseline.json That Suppressed Live Production Secrets
date: '2026-07-13'
category: tech-news
source: Dev.to
url: https://dev.to/dwoitzik/the-gitleaks-baselinejson-that-suppressed-live-production-secrets-528a
tags:
- tech-news
- dev.to
---

## The .gitleaks-baseline.json That Suppressed Live Production Secrets

**Source**: Dev.to

 
  Originally published at  woitzik.dev   
 

 A previous article here covered  setting up gitleaks for homelab secret scanning  - the setup, the pre-commit hook, getting CI to fail on new commits that contain secrets. The setup was correct. The tool was running. The CI was green. And it had been quietly suppressing a live production credential for months. 

 This is the follow-on story: not about getting gitleaks running, but about the specific way a baseline file breaks the guarantees you thi

**Lien**: [Lire](https://dev.to/dwoitzik/the-gitleaks-baselinejson-that-suppressed-live-production-secrets-528a)
