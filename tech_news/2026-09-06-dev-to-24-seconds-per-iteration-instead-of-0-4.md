---
layout: post
title: 24 seconds per iteration instead of 0.4. I paid for six hours of GPU compute
  and trained on CPU the entire time.
date: '2026-09-06'
category: tech-news
source: Dev.to
url: https://dev.to/franciscobooth/24-seconds-per-iteration-instead-of-04-i-paid-for-six-hours-of-gpu-compute-and-trained-on-cpu-the-3p41
tags:
- tech-news
- dev.to
---

## 24 seconds per iteration instead of 0.4. I paid for six hours of GPU compute and trained on CPU the entire time.

**Source**: Dev.to

 Failure 1 — CUDA silently fell back to CPU 

 My training job launched on Vast.ai and ran to completion. Iteration time was 24 seconds instead of 0.4 seconds. CUDA had fallen back to CPU silently. PyTorch logged nothing. I had been billed for six hours of GPU compute while training on an unaccelerated CPU thread the entire time. 

 Failure 2 — HF_HOME on ephemeral disk 

 Every fresh pod re-downloaded base model weights to /root/.cache — the ephemeral container disk wiped on pod shutdown. Same 

**Lien**: [Lire](https://dev.to/franciscobooth/24-seconds-per-iteration-instead-of-04-i-paid-for-six-hours-of-gpu-compute-and-trained-on-cpu-the-3p41)
