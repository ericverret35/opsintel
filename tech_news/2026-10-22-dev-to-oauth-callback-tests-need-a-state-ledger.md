---
layout: post
title: OAuth Callback Tests Need a State Ledger
date: '2026-10-22'
category: tech-news
source: Dev.to
url: https://dev.to/sophiax99/oauth-callback-tests-need-a-state-ledger-li0
tags:
- tech-news
- dev.to
---

## OAuth Callback Tests Need a State Ledger

**Source**: Dev.to

 OAuth callback tests often stop at “the user returned and the token was issued.” That verifies the happy path, but it leaves the most important question unanswered: can the callback prove that this response belongs to the browser session that started the login? 

 The useful mental model is a small state ledger. Each authorization attempt gets a short-lived record. The callback consumes that record only when the provider, redirect URI, browser session,  state , and PKCE proof all agree. This ma

**Lien**: [Lire](https://dev.to/sophiax99/oauth-callback-tests-need-a-state-ledger-li0)
