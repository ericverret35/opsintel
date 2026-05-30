---
layout: post
title: The Moment the Runtime Became Your Enemy
date: '2026-05-30'
category: tech-news
source: Dev.to
url: https://dev.to/built-from-africa/the-moment-the-runtime-became-your-enemy-2do
tags:
- tech-news
- dev.to
---

## The Moment the Runtime Became Your Enemy

**Source**: Dev.to

 
  
  
  The Problem We Were Actually Solving
 

 Our Treasure Hunt Engine indexes 1.2 TB of JSON event logs from Veltrix operators, then answers sub-second queries like give me all log lines where field  error_code = E499  between 2026-05-01T00:00 and 2026-05-07T23:59. Its a classic inverted-index workload. The first version was a Spring Boot monolith running on OpenJDK 21 with G1GC, embedded Lucene, 24 vCPU, 64 GB RAM. We picked it because it was the default stack in 2024. 

 After three mont

**Lien**: [Lire](https://dev.to/built-from-africa/the-moment-the-runtime-became-your-enemy-2do)
