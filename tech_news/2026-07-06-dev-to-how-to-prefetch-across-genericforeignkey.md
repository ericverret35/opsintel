---
layout: post
title: How to Prefetch Across GenericForeignKeys When You Can't Change the Schema
date: '2026-07-06'
category: tech-news
source: Dev.to
url: https://dev.to/acel/how-to-prefetch-across-genericforeignkeys-when-you-cant-change-the-schema-2755
tags:
- tech-news
- dev.to
---

## How to Prefetch Across GenericForeignKeys When You Can't Change the Schema

**Source**: Dev.to

 You don't always control the schema you work with. Sometimes you inherit a codebase where  GenericForeignKey  is threaded through the models, and a migration isn't on the table. Loading a page of 20 audit entries runs ~60 queries because Django's ORM can't prefetch across a GFK. Here's how to fix it without changing a single model. 




 
  
  
  The Problem
 

  GenericForeignKey  lets one table point at rows in multiple other tables without knowing which one at query time. The classic use cas

**Lien**: [Lire](https://dev.to/acel/how-to-prefetch-across-genericforeignkeys-when-you-cant-change-the-schema-2755)
