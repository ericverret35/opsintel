---
layout: post
title: Stop exposing the API server through a NodePort (CKS)
date: '2026-10-06'
category: tech-news
source: Dev.to
url: https://dev.to/thecybersidekick/stop-exposing-the-api-server-through-a-nodeport-cks-1ene
tags:
- tech-news
- dev.to
---

## Stop exposing the API server through a NodePort (CKS)

**Source**: Dev.to

 
  
  
  Stop exposing the API server through a NodePort (CKS)
 

 Lesson three of the CKS series. A security review found the Kubernetes API server reachable through a NodePort, and your job is to put it back behind a ClusterIP. It is one line in a manifest, plus a second step that trips up most people, because the API server will not fix the Service for you. Let's do it on a real control plane. 

 🎥  Watch the video:   https://www.youtube.com/watch?v=GWOuoCNDZq4  

 This is a CKS Cluster Setu

**Lien**: [Lire](https://dev.to/thecybersidekick/stop-exposing-the-api-server-through-a-nodeport-cks-1ene)
