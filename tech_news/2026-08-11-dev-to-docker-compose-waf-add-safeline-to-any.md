---
layout: post
title: 'Docker Compose WAF: Add SafeLine to Any Existing Stack in 3 Steps'
date: '2026-08-11'
category: tech-news
source: Dev.to
url: https://dev.to/lialiago/docker-compose-waf-add-safeline-to-any-existing-stack-in-3-steps-np5
tags:
- tech-news
- dev.to
---

## Docker Compose WAF: Add SafeLine to Any Existing Stack in 3 Steps

**Source**: Dev.to

 
  
  
  The Situation
 

 You already have a Docker Compose stack running: Nginx + your app + PostgreSQL + Redis. It works. You don't want to rebuild it. But you want WAF protection in front. 

 Here's how to add SafeLine to an existing Docker Compose project without disrupting anything. 

 
  
  
  Step 1: Create a Shared Network
 



 
   # docker-compose.yml (add to your existing file) 
 networks  : 
   webnet  : 
     driver  :   bridge 
  

 



 Connect your existing services to this net

**Lien**: [Lire](https://dev.to/lialiago/docker-compose-waf-add-safeline-to-any-existing-stack-in-3-steps-np5)
