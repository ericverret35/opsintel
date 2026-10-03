---
layout: post
title: Why Your Kubernetes HPA Won't Scale Down (It's Probably Not Stuck)
date: '2026-10-03'
category: tech-news
source: Dev.to
url: https://dev.to/polasamyeng/why-your-kubernetes-hpa-wont-scale-down-its-probably-not-stuck-5cmn
tags:
- tech-news
- dev.to
---

## Why Your Kubernetes HPA Won't Scale Down (It's Probably Not Stuck)

**Source**: Dev.to

 You scaled up under load, traffic dropped ten minutes ago, and your HPA is still sitting at 8 replicas instead of 2. First instinct: something's broken. Second instinct, after  kubectl describe hpa  shows nothing wrong: confusion. 

 It's probably not stuck. It's doing exactly what it's configured to do — you just never configured it. 

 
  
  
  The default nobody sets on purpose
 

 If you don't define a  behavior.scaleDown  block on your HPA, Kubernetes falls back to a 300-second stabilizati

**Lien**: [Lire](https://dev.to/polasamyeng/why-your-kubernetes-hpa-wont-scale-down-its-probably-not-stuck-5cmn)
