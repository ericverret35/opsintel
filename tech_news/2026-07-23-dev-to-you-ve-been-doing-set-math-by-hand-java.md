---
layout: post
title: You've been doing Set math by hand. JavaScript finally shipped `.union()`,
  `.intersection()`, and friends.
date: '2026-07-23'
category: tech-news
source: Dev.to
url: https://dev.to/parsajiravand/youve-been-doing-set-math-by-hand-javascript-finally-shipped-union-intersection-and-476
tags:
- tech-news
- dev.to
---

## You've been doing Set math by hand. JavaScript finally shipped `.union()`, `.intersection()`, and friends.

**Source**: Dev.to

 You've written some version of this: 
 

 
   const   intersection   =   new   Set  ([...  setA  ].  filter  (  x   =&gt;   setB  .  has  (  x  ))); 
 const   difference     =   new   Set  ([...  setA  ].  filter  (  x   =&gt;   !  setB  .  has  (  x  ))); 
 const   union          =   new   Set  ([...  setA  ,   ...  setB  ]); 
  

 



 It works. It's also four lines of manual iteration for operations any set-theory textbook covers in a sentence. JavaScript's  Set  shipped in ES6 — ten years a

**Lien**: [Lire](https://dev.to/parsajiravand/youve-been-doing-set-math-by-hand-javascript-finally-shipped-union-intersection-and-476)
