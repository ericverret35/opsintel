---
layout: post
title: How Does useEffect Actually Work?
date: '2026-09-01'
category: tech-news
source: Dev.to
url: https://dev.to/tanu_priya/how-does-useeffect-actually-work-3c53
tags:
- tech-news
- dev.to
---

## How Does useEffect Actually Work?

**Source**: Dev.to

 If you've worked with React for a while, you've probably written something like this: 
 

 
   useEffect  (()   =&gt;   { 
   fetchUser  (); 
 },   []); 
  

 



 It looks simple. 

 But then the questions start: 

 
 Why does  useEffect  run twice in development? 
 Why does it sometimes run again when I didn't expect it? 
 What exactly does the dependency array do? 
 Why does adding a dependency suddenly create an infinite loop? 
 Why do we need a cleanup function? 
 And perhaps the biggest q

**Lien**: [Lire](https://dev.to/tanu_priya/how-does-useeffect-actually-work-3c53)
