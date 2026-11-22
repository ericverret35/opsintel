---
layout: post
title: A check that refused its own tests
date: '2026-11-22'
category: tech-news
source: Dev.to
url: https://dev.to/ilya_mozerov_867dbdd91feb/a-check-that-refused-its-own-tests-3f3m
tags:
- tech-news
- dev.to
---

## A check that refused its own tests

**Source**: Dev.to

 Mishe keeps a small set of automatic checks that run on a timer and publish a verdict: GREEN, RED, or UNKNOWN. One of them scans our public articles for private details before they can be trusted. This week the review of a change to that check turned up a defect in the check's own tests, and the way it was caught is worth describing. 

 
  
  
  What happened
 

 A change to the privacy check went through the delivery path. An independent review refused it. The reviewer's verdict was that the t

**Lien**: [Lire](https://dev.to/ilya_mozerov_867dbdd91feb/a-check-that-refused-its-own-tests-3f3m)
