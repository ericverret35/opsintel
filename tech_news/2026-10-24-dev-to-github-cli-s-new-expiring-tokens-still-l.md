---
layout: post
title: GitHub CLI's New Expiring Tokens Still Leave Your Refresh Token Exposed to
  Malware
date: '2026-10-24'
category: tech-news
source: Dev.to
url: https://dev.to/suzukishunsuke/github-clis-new-expiring-tokens-still-leave-your-refresh-token-exposed-to-malware-2had
tags:
- tech-news
- dev.to
---

## GitHub CLI's New Expiring Tokens Still Leave Your Refresh Token Exposed to Malware

**Source**: Dev.to

 GitHub CLI (gh) recently added short-lived access tokens that are refreshed automatically. It is a public preview and opt-in for now, but it is planned to become the default. 

  https://github.blog/changelog/2026-10-21-github-cli-opt-in-to-expiring-auto-refreshing-oauth-tokens/  

 This is a welcome change: a leaked access token now stops working within eight hours. 
But the refresh token is a different story. 
It lives for months, and gh stores it in the OS keyring, where on macOS any process

**Lien**: [Lire](https://dev.to/suzukishunsuke/github-clis-new-expiring-tokens-still-leave-your-refresh-token-exposed-to-malware-2had)
