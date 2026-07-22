---
layout: post
title: You keep escaping the Promise constructor. `Promise.withResolvers` does it
  right.
date: '2026-07-22'
category: tech-news
source: Dev.to
url: https://dev.to/parsajiravand/you-keep-escaping-the-promise-constructor-promisewithresolvers-does-it-right-31c1
tags:
- tech-news
- dev.to
---

## You keep escaping the Promise constructor. `Promise.withResolvers` does it right.

**Source**: Dev.to

 Every JavaScript developer has written this at least once: 
 

 
   let   resolve  ,   reject  ; 
 const   promise   =   new   Promise  ((  res  ,   rej  )   =&gt;   { 
   resolve   =   res  ; 
   reject   =   rej  ; 
 }); 

 // Later… 
 eventBus  .  on  (  '  done  '  ,   ()   =&gt;   resolve  (  result  )); 
  

 



 You need to trigger the Promise from outside the constructor — from an event listener, a callback, or a message handler. So you capture  resolve  and  reject  by leaking them in

**Lien**: [Lire](https://dev.to/parsajiravand/you-keep-escaping-the-promise-constructor-promisewithresolvers-does-it-right-31c1)
