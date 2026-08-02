---
layout: post
title: 943 bytes that answer HTTP
date: '2026-08-02'
category: tech-news
source: Dev.to
url: https://dev.to/arcker/943-bytes-that-answer-http-2f3f
tags:
- tech-news
- dev.to
---

## 943 bytes that answer HTTP

**Source**: Dev.to

  Verbose is a small experimental language I build  — its compiler proves properties about your code (termination, sound types, declared effects) and emits tiny x86-64 machine code: no runtime, no GC, no libc. This post stands on its own. 

 Picture a 943-byte file. Smaller than a long text message. You run it and send this: 
 

 
  GET / HTTP/1.0
  

 



 It answers: 
 

 
  HTTP/1.0 200 OK
Content-Length: 29

Hello from Verbose over HTTP!
  

 



 No Node, no Python, no nginx in front. No ru

**Lien**: [Lire](https://dev.to/arcker/943-bytes-that-answer-http-2f3f)
