---
layout: post
title: Four HTTP security headers every WordPress site should set
date: '2026-06-02'
category: tech-news
source: Dev.to
url: https://dev.to/jeremy-burgos/four-http-security-headers-every-wordpress-site-should-set-27pd
tags:
- tech-news
- dev.to
---

## Four HTTP security headers every WordPress site should set

**Source**: Dev.to

 
 TL;DR: Four response headers, a few minutes of work, most of the header-level security gap closed. Exact values below, plus a one-line curl to check any site. 
 

 Run this against your own site first: 
 

 
  curl  -I   -s  https://yoursite.com |  grep   -i   -E   'strict-transport|x-content|x-frame|referrer' 
  

 



 Whatever does not come back is your to-do list. These four headers are public on every request and contain nothing sensitive, so you can check mine, I can check yours, and ne

**Lien**: [Lire](https://dev.to/jeremy-burgos/four-http-security-headers-every-wordpress-site-should-set-27pd)
