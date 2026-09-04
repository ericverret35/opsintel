---
layout: post
title: A Wildcard in Your next.config Image remotePatterns Might Turn Your Site Into
  an SSRF Proxy
date: '2026-09-04'
category: tech-news
source: Dev.to
url: https://dev.to/anas_sheikh_2/a-wildcard-in-your-nextconfig-image-remotepatterns-might-turn-your-site-into-an-ssrf-proxy-3nc1
tags:
- tech-news
- dev.to
---

## A Wildcard in Your next.config Image remotePatterns Might Turn Your Site Into an SSRF Proxy

**Source**: Dev.to

  next/image  optimizing external images is genuinely convenient, resizing, format conversion, all handled automatically through Next.js's built-in image optimization endpoint. That endpoint fetches the remote image server-side before serving the optimized version to the browser, and that server-side fetch is exactly the mechanism that becomes a real problem if  remotePatterns  is configured too loosely. 

 
  
  
  The Configuration That Looks Convenient
 



 
   // next.config.ts 
 const   ne

**Lien**: [Lire](https://dev.to/anas_sheikh_2/a-wildcard-in-your-nextconfig-image-remotepatterns-might-turn-your-site-into-an-ssrf-proxy-3nc1)
