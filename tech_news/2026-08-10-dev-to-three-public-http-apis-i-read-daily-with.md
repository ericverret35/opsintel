---
layout: post
title: Three public HTTP APIs I read daily without registering for a key
date: '2026-08-10'
category: tech-news
source: Dev.to
url: https://dev.to/morinaga/three-public-http-apis-i-read-daily-without-registering-for-a-key-1aid
tags:
- tech-news
- dev.to
---

## Three public HTTP APIs I read daily without registering for a key

**Source**: Dev.to

 My daily trends fetch is a Node.js script that runs in GitHub Actions, hits three APIs, and writes a JSON file that feeds my X-drafts pipeline later in the day. None of the three sources require an API key. No OAuth flow, no dashboard signup, no rate-limit token to rotate. 

 That sounds trivial, but it matters for CI pipelines. Every API key stored in GitHub Secrets is a secret that can expire, a secret that has to be rotated when a team member leaves, a secret that creates a failure surface. 

**Lien**: [Lire](https://dev.to/morinaga/three-public-http-apis-i-read-daily-without-registering-for-a-key-1aid)
