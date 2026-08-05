---
layout: post
title: You're collecting async iterable results with a for-await loop. `Array.fromAsync`
  does it in one call.
date: '2026-08-05'
category: tech-news
source: Dev.to
url: https://dev.to/parsajiravand/youre-collecting-async-iterable-results-with-a-for-await-loop-arrayfromasync-does-it-in-one-405e
tags:
- tech-news
- dev.to
---

## You're collecting async iterable results with a for-await loop. `Array.fromAsync` does it in one call.

**Source**: Dev.to

 When you have an async iterable — a  ReadableStream , a generator that fetches paginated results, a database cursor — and you need its values in a plain array, you reach for a loop. 
 

 
   const   results   =   []; 
 for   await   (  const   item   of   asyncSource  )   { 
   results  .  push  (  item  ); 
 } 
  

 



 That works. But it's four lines of ceremony for "give me an array of everything this produces."  Array.fromAsync  is the one-liner that's been missing. 

 
  
  
  The spread 

**Lien**: [Lire](https://dev.to/parsajiravand/youre-collecting-async-iterable-results-with-a-for-await-loop-arrayfromasync-does-it-in-one-405e)
