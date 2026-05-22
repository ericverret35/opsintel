---
layout: post
title: Running LTX-2.3 Alongside TTS on a Single 96GB GPU with a Cold-Start Architecture
date: '2026-05-22'
category: tech-news
source: Dev.to
url: https://dev.to/shinji_shimizu_bb51276a5e/running-ltx-23-alongside-tts-on-a-single-96gb-gpu-with-a-cold-start-architecture-2ee3
tags:
- tech-news
- dev.to
---

## Running LTX-2.3 Alongside TTS on a Single 96GB GPU with a Cold-Start Architecture

**Source**: Dev.to

 When integrating LTX-2.3 (a 22B audio-to-video model) into a voice roleplay product, I ran straight into a VRAM wall. The classic dead-end: running it as a persistent server ate 86 GiB, instantly OOM-ing the TTS / Ditto / MuseTalk stack sharing the same GPU. This is the story of switching to a cold-start design that idles at 0 GiB and peaks at 40 GiB. 

 Hardware: RTX Pro 6000 Blackwell Max-Q (94.97 GiB). Software:  LTX-2 official repo  and bitsandbytes 0.49.1. 

 
  
  
  What I Was Trying to 

**Lien**: [Lire](https://dev.to/shinji_shimizu_bb51276a5e/running-ltx-23-alongside-tts-on-a-single-96gb-gpu-with-a-cold-start-architecture-2ee3)
