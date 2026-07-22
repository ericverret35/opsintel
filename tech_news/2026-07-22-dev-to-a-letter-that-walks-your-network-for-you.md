---
layout: post
title: 'A letter that walks your network for you: reproducing a fresh Roundcube SSRF
  on a live lab'
date: '2026-07-22'
category: tech-news
source: Dev.to
url: https://dev.to/cynepmyx/a-letter-that-walks-your-network-for-you-reproducing-a-fresh-roundcube-ssrf-on-a-live-lab-1357
tags:
- tech-news
- dev.to
---

## A letter that walks your network for you: reproducing a fresh Roundcube SSRF on a live lab

**Source**: Dev.to

 You open an email. While you are reading it, your mail server is already knocking on an internal address you never handed it, because the email told it to. Not a thought experiment. I reproduced it on a lab and caught the request in a log. 

 Reading an email stopped being a passive act a long time ago. The client parses MIME, renders text into HTML, pulls in styles, shows attachments, turns addresses and links into clickable ones. Every one of those steps is code that runs over data a stranger

**Lien**: [Lire](https://dev.to/cynepmyx/a-letter-that-walks-your-network-for-you-reproducing-a-fresh-roundcube-ssrf-on-a-live-lab-1357)
