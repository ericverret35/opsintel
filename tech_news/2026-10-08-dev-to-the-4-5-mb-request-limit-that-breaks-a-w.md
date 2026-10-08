---
layout: post
title: The 4.5 MB request limit that breaks a working PDF merge on Vercel
date: '2026-10-08'
category: tech-news
source: Dev.to
url: https://dev.to/pdfops/the-45-mb-request-limit-that-breaks-a-working-pdf-merge-on-vercel-3ken
tags:
- tech-news
- dev.to
---

## The 4.5 MB request limit that breaks a working PDF merge on Vercel

**Source**: Dev.to

 A PDF merge endpoint that works every time on a laptop can start returning 413 the moment it moves onto Vercel, with no body in the response to explain why. The input files look reasonable, the handler code hasn't changed, and the identical request against a local dev server still succeeds. The cause is a cap on the whole request body that Vercel enforces before a serverless function's own code runs at all, so no amount of debugging inside the handler will find it. The handler never gets invoke

**Lien**: [Lire](https://dev.to/pdfops/the-45-mb-request-limit-that-breaks-a-working-pdf-merge-on-vercel-3ken)
