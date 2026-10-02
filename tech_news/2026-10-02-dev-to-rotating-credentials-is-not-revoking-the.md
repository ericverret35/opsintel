---
layout: post
title: Rotating Credentials Is Not Revoking Them. The Revocation Unit Decides Whether
  You Can.
date: '2026-10-02'
category: tech-news
source: Dev.to
url: https://dev.to/ntctech/rotating-credentials-is-not-revoking-them-the-revocation-unit-decides-whether-you-can-1c5o
tags:
- tech-news
- dev.to
---

## Rotating Credentials Is Not Revoking Them. The Revocation Unit Decides Whether You Can.

**Source**: Dev.to

 The revocation unit decides whether credential rotation can ever be atomic. It is the scope one revoke action removes: a token, an identity, or a trust root. Most teams treat rotation and revocation as one operation. They aren't. Rotation issues new secrets. Revocation removes the authority of everything that could have used the old ones, and it works only if the architecture can name that set and remove it in a single step. 

     

  The Server Was Fixed. Persistent Access Wasn't.  covered wh

**Lien**: [Lire](https://dev.to/ntctech/rotating-credentials-is-not-revoking-them-the-revocation-unit-decides-whether-you-can-1c5o)
