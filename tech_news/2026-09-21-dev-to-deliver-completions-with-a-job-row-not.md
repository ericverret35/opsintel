---
layout: post
title: Deliver Completions With a Job Row, Not a Held Connection
date: '2026-09-21'
category: tech-news
source: Dev.to
url: https://dev.to/kongkong1/deliver-completions-with-a-job-row-not-a-held-connection-5b93
tags:
- tech-news
- dev.to
---

## Deliver Completions With a Job Row, Not a Held Connection

**Source**: Dev.to

 Last Tuesday I sat with a teammate who clicked Generate on a supposedly simple report screen. The spinner behaved like a prayer, nginx hit sixty seconds, and the gateway returned 504 while a model process kept talking to nobody. Did the user get a paragraph? No. Did a refresh spend another free inference call on the same prompt? Yes, immediately, because the POST had been the product. 

 I am done treating that architecture as a prototype shortcut. If a browser is holding a TCP connection while

**Lien**: [Lire](https://dev.to/kongkong1/deliver-completions-with-a-job-row-not-a-held-connection-5b93)
