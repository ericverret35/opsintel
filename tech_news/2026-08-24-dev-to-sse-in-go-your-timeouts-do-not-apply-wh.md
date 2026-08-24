---
layout: post
title: 'SSE in Go: Your Timeouts Do Not Apply Where You Think'
date: '2026-08-24'
category: tech-news
source: Dev.to
url: https://dev.to/julesrobineau/sse-in-go-your-timeouts-do-not-apply-where-you-think-3gp8
tags:
- tech-news
- dev.to
---

## SSE in Go: Your Timeouts Do Not Apply Where You Think

**Source**: Dev.to

 An SSE stream is an HTTP request that never ends. Every default you did not touch is working against it. 

 
  TL;DR : your SSE endpoint breaks twice before it reaches your logic. Once because the  Connection  header is illegal in HTTP/2. Once because your Go server's default timeouts cut the stream at 30 seconds. And if you stay on HTTP/1.1, a permanent stream freezes the rest of your page. In August 2026, Go patched a flaw where a timeout was not applied to HTTP/2 connections. Same lesson: a 

**Lien**: [Lire](https://dev.to/julesrobineau/sse-in-go-your-timeouts-do-not-apply-where-you-think-3gp8)
