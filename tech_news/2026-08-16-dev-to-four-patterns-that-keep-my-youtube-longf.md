---
layout: post
title: Four patterns that keep my YouTube longform JSON queue from going stale
date: '2026-08-16'
category: tech-news
source: Dev.to
url: https://dev.to/morinaga/four-patterns-that-keep-my-youtube-longform-json-queue-from-going-stale-2750
tags:
- tech-news
- dev.to
---

## Four patterns that keep my YouTube longform JSON queue from going stale

**Source**: Dev.to

 I manage the YouTube longform queue for my BuilderStack channel as JSON files in  content/yt-longform-queue/ . A spec file lands there when a generator script commits a new dialogue; the publish workflow picks the file, renders it to MP4, uploads it, then moves the file to  uploaded/ . No external queue service, no database rows, no management dashboard. 

 This has worked for three months without a major incident. Four patterns kept it from collapsing. 

 
  
  
  Archetype-priority picking, n

**Lien**: [Lire](https://dev.to/morinaga/four-patterns-that-keep-my-youtube-longform-json-queue-from-going-stale-2750)
