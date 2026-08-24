---
layout: post
title: Your canvas.toBlob might be silently handing you a PNG
date: '2026-08-24'
category: tech-news
source: Dev.to
url: https://dev.to/pm_cheng_3f36acecfb9c59f5/your-canvastoblob-might-be-silently-handing-you-a-png-27bo
tags:
- tech-news
- dev.to
---

## Your canvas.toBlob might be silently handing you a PNG

**Source**: Dev.to

 A user told me the  .webp  files my tool produced wouldn't open on their desktop. I opened one in a hex editor. First four bytes:   
89 50 4E 47 . 
It was a PNG. With a  .webp  extension. 
The encoder wasn't broken. I had simply never checked whether the browser actually did what I asked. 
 
  
  
  The spec says it's allowed to do this
 

 Here's the code. Nothing looks wrong with it: 
 

 
   canvas  .  toBlob  (  blob   =&gt;   { 
   download  (  blob  ,   '  output.webp  '  ); 
 },   '  ima

**Lien**: [Lire](https://dev.to/pm_cheng_3f36acecfb9c59f5/your-canvastoblob-might-be-silently-handing-you-a-png-27bo)
