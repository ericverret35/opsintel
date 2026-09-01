---
layout: post
title: A calendar library returned the same answer for every year — and my tests agreed
  with it
date: '2026-09-01'
category: tech-news
source: Dev.to
url: https://dev.to/beachcombers/a-calendar-library-returned-the-same-answer-for-every-year-and-my-tests-agreed-with-it-1j93
tags:
- tech-news
- dev.to
---

## A calendar library returned the same answer for every year — and my tests agreed with it

**Source**: Dev.to

 I build a Korean saju (BaZi) service. The whole pitch is that the numbers are computed deterministically and only the prose is written by a model, so the calculation layer is the one part that is not allowed to be vaguely right. 

 Two days ago I found out it had been wrong for five years of birthdays, and that my test suite had been cheerfully confirming it the entire time. 

 
  
  
  What the function was supposed to do
 

 A saju chart's year and month pillars do not change on January 1st. 

**Lien**: [Lire](https://dev.to/beachcombers/a-calendar-library-returned-the-same-answer-for-every-year-and-my-tests-agreed-with-it-1j93)
