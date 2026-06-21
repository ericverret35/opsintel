---
layout: post
title: '1.5.3 Join Nodes: NestLoop, HashJoin, MergeJoin'
date: '2026-06-21'
category: tech-news
source: Dev.to
url: https://dev.to/joonghyukshin/153-join-nodes-nestloop-hashjoin-mergejoin-2fek
tags:
- tech-news
- dev.to
---

## 1.5.3 Join Nodes: NestLoop, HashJoin, MergeJoin

**Source**: Dev.to

 A scan node sits at the leaf of the tree and pulls rows from a single table. A join node sits in the middle and brings together the rows that its two children send up. It takes one row from  users , one row from  orders , checks whether they belong to the same user, and if they match, emits the combined row. PostgreSQL has three nodes for this one job: NestLoop, HashJoin, and MergeJoin. The reason a single task splits into three nodes is much like the reason scans did. There is more than one wa

**Lien**: [Lire](https://dev.to/joonghyukshin/153-join-nodes-nestloop-hashjoin-mergejoin-2fek)
