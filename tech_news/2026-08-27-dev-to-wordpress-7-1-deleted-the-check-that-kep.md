---
layout: post
title: WordPress 7.1 deleted the check that kept classic editors un-iframed. Run this
  grep.
date: '2026-08-27'
category: tech-news
source: Dev.to
url: https://dev.to/max_soskind_5b8cd4ab954ab/wordpress-71-deleted-the-check-that-kept-classic-editors-un-iframed-run-this-grep-1flc
tags:
- tech-news
- dev.to
---

## WordPress 7.1 deleted the check that kept classic editors un-iframed. Run this grep.

**Source**: Dev.to

 WordPress 7.1 took down a client's editor last week. Every custom ACF block moved its fields to the sidebar, and on one site they stopped saving with no error at all. 

 Not an ACF bug. One line of core JavaScript. 

 Through 7.0.x the editor iframed the canvas only if  every  block in the post was API v3 or higher. A default ACF block is v2, so one of them kept the whole canvas un-iframed. That was the escape hatch. Most of us never knew we were standing on it. 

 In 7.1  disableIframe  does n

**Lien**: [Lire](https://dev.to/max_soskind_5b8cd4ab954ab/wordpress-71-deleted-the-check-that-kept-classic-editors-un-iframed-run-this-grep-1flc)
