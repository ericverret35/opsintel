---
layout: post
title: 'Cronflower: run a DAG workflow across your cluster, instead of chaining cron
  jobs'
date: '2026-09-20'
category: tech-news
source: Dev.to
url: https://dev.to/paganini2008/stop-chaining-cron-jobs-run-a-dag-workflow-across-your-cluster-1ibi
tags:
- tech-news
- dev.to
---

## Cronflower: run a DAG workflow across your cluster, instead of chaining cron jobs

**Source**: Dev.to

 Every team ends up here. One cron job at 02:00 charges the orders. Another at 02:15 ships them, set 
fifteen minutes later because that's  usually  long enough for the first one to finish. There's no 
real dependency between them, no shared data, and no way to see, after the fact, whether step two ran 
because step one actually succeeded or just because the clock moved. 

 That's the wall plain cron hits: it schedules single jobs, it can't orchestrate a flow of them. 

  cronflower  is an open-

**Lien**: [Lire](https://dev.to/paganini2008/stop-chaining-cron-jobs-run-a-dag-workflow-across-your-cluster-1ibi)
