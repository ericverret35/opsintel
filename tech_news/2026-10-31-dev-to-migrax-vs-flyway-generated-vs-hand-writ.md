---
layout: post
title: 'Migrax vs Flyway: generated vs hand-written migrations'
date: '2026-10-31'
category: tech-news
source: Dev.to
url: https://dev.to/fsmutimeer/migrax-vs-flyway-generated-vs-hand-written-migrations-126j
tags:
- tech-news
- dev.to
---

## Migrax vs Flyway: generated vs hand-written migrations

**Source**: Dev.to

 Flyway and Migrax both keep a database schema in numbered SQL files, apply them in order and record what ran. The difference is where the SQL comes from. With Flyway you write every migration yourself. With Migrax you change your JPA entities and it writes the migration, which you then review. 

 This article makes the same change with both, on the same PostgreSQL database, and compares what each one does along the way. It also says where Flyway is the better choice. 

 
  Tested with:  Flyway 

**Lien**: [Lire](https://dev.to/fsmutimeer/migrax-vs-flyway-generated-vs-hand-written-migrations-126j)
