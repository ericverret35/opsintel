---
layout: post
title: The token is valid — but your headless Claude Code agent just 401'd forever
date: '2026-06-28'
category: tech-news
source: Dev.to
url: https://dev.to/drickon/the-token-is-valid-but-your-headless-claude-code-agent-just-401d-forever-48ip
tags:
- tech-news
- dev.to
---

## The token is valid — but your headless Claude Code agent just 401'd forever

**Source**: Dev.to

  TL;DR:  A static OAuth access token can return HTTP 200 on a raw  /v1/messages  call at the exact instant a long-running Claude Code instance using that  same token  gets 401 "Invalid authentication credentials" — because the rejection is bound to the instance's own server-side session identity, not the token. Worse, once it 401s the instance hard-latches and never self-recovers until you restart the process, so any "is the token valid?" probe is structurally blind to the problem. 

 
  
  
  

**Lien**: [Lire](https://dev.to/drickon/the-token-is-valid-but-your-headless-claude-code-agent-just-401d-forever-48ip)
