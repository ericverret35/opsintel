---
layout: post
title: Five AI coding tools, five completely different ways to break
date: '2026-08-18'
category: tech-news
source: Dev.to
url: https://dev.to/xiaodong_zhang_bd8dc835b3/five-ai-coding-tools-five-completely-different-ways-to-break-bc7
tags:
- tech-news
- dev.to
---

## Five AI coding tools, five completely different ways to break

**Source**: Dev.to

 I've now routed five different AI coding tools through a proxy layer. Each one broke differently. None of them told me why. 

 Writing this partly as a reference for myself, partly because the failure modes turn out to be genuinely interesting — they say a lot about how these tools are built. 

 
  
  
  Claude Code: reads config once, then never again
 

 The simplest of the five. Config lives in  ~/.claude/settings.json , two keys get modified: 
 

 
   env.ANTHROPIC_BASE_URL 
 env.ANTHROPIC_

**Lien**: [Lire](https://dev.to/xiaodong_zhang_bd8dc835b3/five-ai-coding-tools-five-completely-different-ways-to-break-bc7)
