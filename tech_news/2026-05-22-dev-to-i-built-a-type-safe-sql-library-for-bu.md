---
layout: post
title: '# I built a type-safe SQL library for Bun — no ORM, no codegen, just SQL (using
  Claude Code)'
date: '2026-05-22'
category: tech-news
source: Dev.to
url: https://dev.to/phonemyatt/-i-built-a-type-safe-sql-library-for-bun-no-orm-no-codegen-just-sql-1k43
tags:
- tech-news
- dev.to
---

## # I built a type-safe SQL library for Bun — no ORM, no codegen, just SQL (using Claude Code)

**Source**: Dev.to

 I've been using Bun for a while and kept running into the same problem: every SQL library either requires Node.js internals, leans heavily on an ORM abstraction I don't want, or generates types from a schema file at build time. 

 So I built  squn  — a lightweight, type-safe SQL query library that works natively with Bun's built-in database clients. 

 
  
  
  The core idea
 

 Every query goes through a tagged template literal called  sql . Interpolated values always become bound parameters —

**Lien**: [Lire](https://dev.to/phonemyatt/-i-built-a-type-safe-sql-library-for-bun-no-orm-no-codegen-just-sql-1k43)
