---
layout: post
title: What ref() and reactive() Are Actually For
date: '2026-07-07'
category: tech-news
source: Dev.to
url: https://dev.to/ysndmr/what-ref-and-reactive-are-actually-for-c52
tags:
- tech-news
- dev.to
---

## What ref() and reactive() Are Actually For

**Source**: Dev.to

 Vue 3 gives you two ways to make something reactive:  ref()  and  reactive() . The docs explain the difference clearly enough. What they don't tell you is which one to reach for by default. 

 The short answer:   ref() , almost always.   reactive()  for specific situations where you know what you're trading away. 

 Here's the problem with  reactive() . It loses reactivity when you destructure it or reassign the root object, which catches people off guard more than it should. 
 

 
   const   s

**Lien**: [Lire](https://dev.to/ysndmr/what-ref-and-reactive-are-actually-for-c52)
