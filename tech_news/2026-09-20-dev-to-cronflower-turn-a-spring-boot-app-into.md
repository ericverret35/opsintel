---
layout: post
title: 'Cronflower: turn a Spring Boot app into a distributed cron cluster'
date: '2026-09-20'
category: tech-news
source: Dev.to
url: https://dev.to/paganini2008/turn-a-spring-boot-app-into-a-distributed-cron-cluster-3pd0
tags:
- tech-news
- dev.to
---

## Cronflower: turn a Spring Boot app into a distributed cron cluster

**Source**: Dev.to

  @Scheduled  is fine until it isn't. It runs in one JVM, so the moment you scale to two instances the 
job fires twice. It has no retry, no timeout, no record of what ran, and if the box reboots at 02:00 
the nightly rollup just quietly doesn't happen. You end up bolting on Quartz, a database, a lock 
table, and a dashboard you wrote yourself. 

  cronflower  is that whole stack, open source: a distributed, stateful scheduler for Spring Boot 
with a web console, that forms its own cluster and n

**Lien**: [Lire](https://dev.to/paganini2008/turn-a-spring-boot-app-into-a-distributed-cron-cluster-3pd0)
