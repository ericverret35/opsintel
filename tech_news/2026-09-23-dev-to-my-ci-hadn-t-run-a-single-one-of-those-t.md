---
layout: post
title: My CI hadn't run a single one of those tests in two months and stayed green
  the whole time
date: '2026-09-23'
category: tech-news
source: Dev.to
url: https://dev.to/juanauriti/my-ci-hadnt-run-a-single-one-of-those-tests-in-two-months-and-stayed-green-the-whole-time-n15
tags:
- tech-news
- dev.to
---

## My CI hadn't run a single one of those tests in two months and stayed green the whole time

**Source**: Dev.to

 I added a dependency to a test helper and forgot to declare it in the dev extra. Locally it was already installed, so everything passed. In CI it wasn't, and the tests that needed it did not fail. 

 They skipped. 

 Skips exit 0. The checkmark stayed green for two months. 

 
  
  
  Why it skips instead of failing
 

 The pattern is one line, it's in every codebase, and it's usually correct: 
 

 
   aiosqlite   =   pytest  .  importorskip  (  "  aiosqlite  "  ) 
  

 



 That line means:  t

**Lien**: [Lire](https://dev.to/juanauriti/my-ci-hadnt-run-a-single-one-of-those-tests-in-two-months-and-stayed-green-the-whole-time-n15)
