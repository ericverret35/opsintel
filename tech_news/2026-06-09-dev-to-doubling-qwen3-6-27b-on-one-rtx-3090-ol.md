---
layout: post
title: 'Doubling Qwen3.6-27B on One RTX 3090: ollama llama.cpp + MTP, Lever by Lever
  (35.7 80.2 tok/s)'
date: '2026-06-09'
category: tech-news
source: Dev.to
url: https://dev.to/sysoft/doubling-qwen36-27b-on-one-rtx-3090-ollama-llamacpp-mtp-lever-by-lever-357-802-toks-4i8
tags:
- tech-news
- dev.to
---

## Doubling Qwen3.6-27B on One RTX 3090: ollama llama.cpp + MTP, Lever by Lever (35.7 80.2 tok/s)

**Source**: Dev.to

 
 A reader on my  last post  said Ollama was leaving a lot on the table — that a tuned backend with multi-token prediction (MTP) could roughly double my 3090's throughput. So I went and measured it, one lever at a time. The short version: they were right, the  2.25× is real , and below is the exact path that got me there on my box. 
 

 
  
  
  TL;DR
 

 On a single RTX 3090, Qwen3.6-27B generation went from  35.7 tok/s (Ollama)  to  80.2 tok/s (llama.cpp + MTP)  — a measured  2.25×  — by stac

**Lien**: [Lire](https://dev.to/sysoft/doubling-qwen36-27b-on-one-rtx-3090-ollama-llamacpp-mtp-lever-by-lever-357-802-toks-4i8)
