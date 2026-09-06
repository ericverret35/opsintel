---
layout: post
title: btoa('café') gives you the wrong bytes, and nothing tells you
date: '2026-09-06'
category: tech-news
source: Dev.to
url: https://dev.to/vish045/btoacafe-gives-you-the-wrong-bytes-and-nothing-tells-you-4i20
tags:
- tech-news
- dev.to
---

## btoa('café') gives you the wrong bytes, and nothing tells you

**Source**: Dev.to

 Run this in your browser console: 
 

 
   btoa  (  '  café  '  ); 
 // 'Y2Fm6Q==' 
  

 



 Now encode the same word as UTF-8 first: 
 

 
   btoa  (  String  .  fromCharCode  (...  new   TextEncoder  ().  encode  (  '  café  '  ))); 
 // 'Y2Fmw6k=' 
  

 



 Same word, two different answers. Both are valid base64. Neither one throws. Only the second is what everyone else means by "café in base64". 

 
  
  
  Why this happens
 

  btoa  and  atob  are old. They work on "binary strings", whe

**Lien**: [Lire](https://dev.to/vish045/btoacafe-gives-you-the-wrong-bytes-and-nothing-tells-you-4i20)
