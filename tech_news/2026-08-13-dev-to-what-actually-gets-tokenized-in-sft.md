---
layout: post
title: What Actually Gets Tokenized in SFT
date: '2026-08-13'
category: tech-news
source: Dev.to
url: https://dev.to/jessiejia11/what-actually-gets-tokenized-in-sft-jbo
tags:
- tech-news
- dev.to
---

## What Actually Gets Tokenized in SFT

**Source**: Dev.to

  tok.apply_chat_template(msgs, add_generation_prompt=True)  

 I have copied that line more times than I can count without thinking about what any of it does. The official example writes it that way, the output looks right, you move on. 

 Then you have to build your own SFT data and compute your own loss mask, and it turns out every piece of that line is load-bearing. I spent today pulling it apart. Notes below. 

 The counterintuitive part first: the model has no idea  messages  exists. 

 
 

**Lien**: [Lire](https://dev.to/jessiejia11/what-actually-gets-tokenized-in-sft-jbo)
