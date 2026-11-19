---
layout: post
title: How to pull a Substack newsletter's posts as Markdown
date: '2026-11-19'
category: tech-news
source: Dev.to
url: https://dev.to/cedarfetch/how-to-pull-a-substack-newsletters-posts-as-markdown-5c83
tags:
- tech-news
- dev.to
---

## How to pull a Substack newsletter's posts as Markdown

**Source**: Dev.to

 You want a newsletter's archive as Markdown files, for offline reading, a search index or a knowledge base. Every Substack publication serves its archive and its posts as JSON, on a  name.substack.com  address and on custom domains, and free posts need no login. 

 
  
  
  The archive endpoint
 

  GET https://&lt;publication&gt;/api/v1/archive?sort=new&amp;limit=25  returns  {"posts": [...], "nextCursor": "..."} . Each post has  id ,  slug ,  title ,  subtitle ,  post_date ,  audience ,  type

**Lien**: [Lire](https://dev.to/cedarfetch/how-to-pull-a-substack-newsletters-posts-as-markdown-5c83)
