---
layout: post
title: Why your AI chat reconnects but your session doesn't
date: '2026-05-27'
category: tech-news
source: Dev.to
url: https://dev.to/ably/why-your-ai-chat-reconnects-but-your-session-doesnt-36jg
tags:
- tech-news
- dev.to
---

## Why your AI chat reconnects but your session doesn't

**Source**: Dev.to

 TL;DR: WebSockets are the right protocol for production AI chat. But the connection is stateless at the session level. When it drops — AWS ALB defaults to 60 seconds, Cloudflare to 100 seconds on Free and Pro plans — all in-flight tokens, tool call results, and agent context disappear. Reconnection logic restores the socket. It doesn't restore the session. That's the gap this post covers. 

 WebSockets are the right protocol for production AI chat. But that fact doesn't prevent the failure most

**Lien**: [Lire](https://dev.to/ably/why-your-ai-chat-reconnects-but-your-session-doesnt-36jg)
