---
layout: post
title: 'MongoDB Indexes Finally Clicked for Me: Understanding Indexes, Compound Indexes
  & the Prefix Rule 🚀'
date: '2026-06-24'
category: tech-news
source: Dev.to
url: https://dev.to/aarthirs/mongodb-indexes-finally-clicked-for-me-understanding-indexes-compound-indexes-the-prefix-rule-1f45
tags:
- tech-news
- dev.to
---

## MongoDB Indexes Finally Clicked for Me: Understanding Indexes, Compound Indexes & the Prefix Rule 🚀

**Source**: Dev.to

 While working on a MERN project, I came across these indexes: 
 

 
   transactionSchema  .  index  ({   user  :   1  ,   date  :   -  1   }); 
 transactionSchema  .  index  ({   user  :   1  ,   type  :   -  1   }); 
 transactionSchema  .  index  ({   user  :   1  ,   category  :   -  1   }); 
  

 



 My first reaction was: 

 
 "Why are we creating 3 different indexes for the same schema? Isn't one index enough?" 
 

 At that time, my understanding was: 

 
 "Indexes help MongoDB find recor

**Lien**: [Lire](https://dev.to/aarthirs/mongodb-indexes-finally-clicked-for-me-understanding-indexes-compound-indexes-the-prefix-rule-1f45)
