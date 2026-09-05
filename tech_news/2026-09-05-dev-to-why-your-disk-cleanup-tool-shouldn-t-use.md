---
layout: post
title: Why your disk cleanup tool shouldn't use rm -rf
date: '2026-09-05'
category: tech-news
source: Dev.to
url: https://dev.to/anidotnet/why-your-disk-cleanup-tool-shouldnt-use-rm-rf-5a3n
tags:
- tech-news
- dev.to
---

## Why your disk cleanup tool shouldn't use rm -rf

**Source**: Dev.to

 A developer machine accumulates build output the way a workshop accumulates sawdust. A  target/  here, a  node_modules/  there, a  build/  in every Flutter app you've ever touched. None of it is precious. All of it is invisible until  df -h  says otherwise. Add up enough projects and it's routinely tens of gigabytes, sitting on an SSD you can't upgrade. 

 The obvious fix is a one-liner everyone eventually writes for themselves: 
 

 
  find  .   -name  node_modules  -type  d  -prune   -exec   

**Lien**: [Lire](https://dev.to/anidotnet/why-your-disk-cleanup-tool-shouldnt-use-rm-rf-5a3n)
