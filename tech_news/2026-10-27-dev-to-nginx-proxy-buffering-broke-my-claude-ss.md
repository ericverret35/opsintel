---
layout: post
title: 'nginx proxy_buffering Broke My Claude SSE Stream: 0.7s to 3.4s TTFT'
date: '2026-10-27'
category: tech-news
source: Dev.to
url: https://dev.to/ji_ai/nginx-proxybuffering-broke-my-claude-sse-stream-07s-to-34s-ttft-30d2
tags:
- tech-news
- dev.to
---

## nginx proxy_buffering Broke My Claude SSE Stream: 0.7s to 3.4s TTFT

**Source**: Dev.to

 On my laptop, the chat app streamed like it should. The first word showed up in under a second and the rest typed itself out. Then I deployed it behind nginx, and the same app sat on a blinking cursor for three, five, sometimes nine seconds before dumping a whole paragraph at once. 

 Nothing was wrong with Claude, and nothing was wrong with my FastAPI code. The cause was nginx proxy_buffering, which is on by default and quietly turns a server-sent events (SSE) stream into a batch job. Fixing i

**Lien**: [Lire](https://dev.to/ji_ai/nginx-proxybuffering-broke-my-claude-sse-stream-07s-to-34s-ttft-30d2)
