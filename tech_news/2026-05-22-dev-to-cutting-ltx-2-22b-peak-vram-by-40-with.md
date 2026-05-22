---
layout: post
title: Cutting LTX-2 22B Peak VRAM by 40% with fp8_cast — and Why optimum-quanto Was
  a Trap
date: '2026-05-22'
category: tech-news
source: Dev.to
url: https://dev.to/shinji_shimizu_bb51276a5e/cutting-ltx-2-22b-peak-vram-by-40-with-fp8cast-and-why-optimum-quanto-was-a-trap-1o8d
tags:
- tech-news
- dev.to
---

## Cutting LTX-2 22B Peak VRAM by 40% with fp8_cast — and Why optimum-quanto Was a Trap

**Source**: Dev.to

 
  
  
  Introduction
 

  LTX-2.3  is a video generation model from Lightricks that includes audio support. In A2V (Audio-to-Video) mode, it takes  a single image + audio + prompt  and generates lip sync, facial expressions, and head/hair motion all at once. Unlike lip-sync-only models like MuseTalk, it can animate an entire scene, which makes it a powerful tool for directing. 

 The catch: the base checkpoint is 22B parameters / 43 GB, and keeping it resident in bf16 with  transformer × 2 sta

**Lien**: [Lire](https://dev.to/shinji_shimizu_bb51276a5e/cutting-ltx-2-22b-peak-vram-by-40-with-fp8cast-and-why-optimum-quanto-was-a-trap-1o8d)
