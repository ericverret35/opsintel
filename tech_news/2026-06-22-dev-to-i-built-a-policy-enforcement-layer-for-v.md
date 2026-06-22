---
layout: post
title: I Built a Policy Enforcement Layer for Vercel's Eve Agent Framework. Here's
  What I Learned About AI Governance the Hard Way.
date: '2026-06-22'
category: tech-news
source: Dev.to
url: https://dev.to/omotayojayone/i-built-a-policy-enforcement-layer-for-vercels-eve-agent-framework-heres-what-i-learned-about-ai-1758
tags:
- tech-news
- dev.to
---

## I Built a Policy Enforcement Layer for Vercel's Eve Agent Framework. Here's What I Learned About AI Governance the Hard Way.

**Source**: Dev.to

 
  
  
  TL;DR
 

 
 Vercel's Eve (2.2k stars, actively developed) is a filesystem-first framework for building durable backend agents — but it ships with no governance layer 
 I built   eve-policy  , an open source policy enforcement library that wires into Eve's  needsApproval  and  execute  lifecycle with four-tier semantics: deny, escalate, audit, allow 
 The most interesting design challenge: Eve's  needsApproval  is synchronous and session-less, while  execute  is async with full session 

**Lien**: [Lire](https://dev.to/omotayojayone/i-built-a-policy-enforcement-layer-for-vercels-eve-agent-framework-heres-what-i-learned-about-ai-1758)
