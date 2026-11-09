---
layout: post
title: Only the Design of a Local LLM Eval Harness Survives — Rebuilding It for Qwen3.8
  27B
date: '2026-11-09'
category: tech-news
source: Dev.to
url: https://dev.to/kohei_wada/only-the-design-of-a-local-llm-eval-harness-survives-rebuilding-it-for-qwen38-27b-24ic
tags:
- tech-news
- dev.to
---

## Only the Design of a Local LLM Eval Harness Survives — Rebuilding It for Qwen3.8 27B

**Source**: Dev.to

 
  
  
  Introduction
 

 Three weeks ago, to settle whether Ornith 1.0 35B (MoE 35B/A3B) deserved to be opencode's default on my RTX 5090, I wrote a harness that makes a model port RFC 6902 (JSON Patch) to Rust ( The 3x faster local LLM that couldn't finish the job ). It was three times faster and matched on quality for one-shot work, but went 0-5 on multi-step agent tasks, and Ornith ended up demoted to a speed lane. 

 Qwen3.8 27B came out, so I ran it through the same harness. I switched: t

**Lien**: [Lire](https://dev.to/kohei_wada/only-the-design-of-a-local-llm-eval-harness-survives-rebuilding-it-for-qwen38-27b-24ic)
