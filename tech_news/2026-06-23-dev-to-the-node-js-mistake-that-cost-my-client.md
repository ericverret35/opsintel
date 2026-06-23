---
layout: post
title: The Node.js Mistake That Cost My Client $3,000 in AWS Bills
date: '2026-06-23'
category: tech-news
source: Dev.to
url: https://dev.to/manolito99/the-nodejs-mistake-that-cost-my-client-3000-in-aws-bills-30a5
tags:
- tech-news
- dev.to
---

## The Node.js Mistake That Cost My Client $3,000 in AWS Bills

**Source**: Dev.to

 Last year I was asked to investigate a startup's AWS bill. 

 It had jumped from roughly $200/month to over $3,000 in a few weeks. 

 Nobody knew why. 

 After digging through logs, metrics, and database traffic, I found the culprit: a polling loop with no backoff strategy. 

 The code looked harmless: 
 

 
   async   function   processQueue  ()   { 
   const   jobs   =   await   getJobs  () 

   for   (  const   job   of   jobs  )   { 
     await   processFile  (  job  ) 
   } 

   processQue

**Lien**: [Lire](https://dev.to/manolito99/the-nodejs-mistake-that-cost-my-client-3000-in-aws-bills-30a5)
