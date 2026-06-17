---
layout: post
title: 'Lie to the Postgres planner: EXPLAIN your query at 10,000 the rows'
date: '2026-06-17'
category: tech-news
source: Dev.to
url: https://dev.to/hitoshi1964/lie-to-the-postgres-planner-explain-your-query-at-10000-the-rows-2gkp
tags:
- tech-news
- dev.to
---

## Lie to the Postgres planner: EXPLAIN your query at 10,000 the rows

**Source**: Dev.to

 Your query is snappy in dev. Then it hits production data and the plan quietly flips from an Index Scan to a Seq Scan, or a Nested Loop to a Hash Join, and everything falls over. The painful part:  you can't see that coming on a dev database with 5,000 rows , because the planner picks plans based on how big it  thinks  the tables are. 

 So let's change what it thinks. 

 
  
  
  The planner runs on  pg_class  statistics
 

 When Postgres plans a query, it doesn't count your rows — it reads ca

**Lien**: [Lire](https://dev.to/hitoshi1964/lie-to-the-postgres-planner-explain-your-query-at-10000-the-rows-2gkp)
