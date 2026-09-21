---
layout: post
title: What's actually inside a Whoosh index? A tour of the on-disk format
date: '2026-09-21'
category: tech-news
source: Dev.to
url: https://dev.to/priyasundaram/whats-actually-inside-a-whoosh-index-a-tour-of-the-on-disk-format-5g6o
tags:
- tech-news
- dev.to
---

## What's actually inside a Whoosh index? A tour of the on-disk format

**Source**: Dev.to

 You call  writer.commit()  and a folder fills up with cryptic files like  MAIN_732lvfydjrsyhh2v.seg  and  _MAIN_1.toc . What are they? Understanding the layout demystifies a lot of search behavior — why commits are cheap, why the first search after many small writes can be slow, and what  optimize=True  actually does. Whoosh is pure Python, so we can just open it up and look. 

 
  
  
  1. Two kinds of files: the TOC and the segments
 

 List an index dir and you'll see: 
 

 
  _MAIN_1.toc   

**Lien**: [Lire](https://dev.to/priyasundaram/whats-actually-inside-a-whoosh-index-a-tour-of-the-on-disk-format-5g6o)
