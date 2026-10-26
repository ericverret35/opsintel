---
layout: post
title: 'Your LLM spend cap is bypassable: X-Forwarded-For vs CloudFront-Viewer-Address,
  and why you also need an origin lock'
date: '2026-10-26'
category: tech-news
source: Dev.to
url: https://dev.to/gabrielm92/your-llm-spend-cap-is-bypassable-x-forwarded-for-vs-cloudfront-viewer-address-and-why-you-also-324e
tags:
- tech-news
- dev.to
---

## Your LLM spend cap is bypassable: X-Forwarded-For vs CloudFront-Viewer-Address, and why you also need an origin lock

**Source**: Dev.to

  If you put a per-user or per-IP free-tier cap in front of a paid call on Lambda behind CloudFront and API Gateway, the obvious key is spoofable, the execute-api URL is a side door, and an in-memory counter overshoots. Here is each bug and its fix.  

 
  
  
  The setup
 

 You run a Lambda behind CloudFront and API Gateway. In front of a paid call — an LLM completion, say — you put a free tier: so many calls per anonymous user per day, then you stop. The counter needs a key. The obvious choic

**Lien**: [Lire](https://dev.to/gabrielm92/your-llm-spend-cap-is-bypassable-x-forwarded-for-vs-cloudfront-viewer-address-and-why-you-also-324e)
