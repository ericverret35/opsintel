---
layout: post
title: 'waitForResponse() timing: the one-line fix with a non-obvious mental model'
date: '2026-06-05'
category: tech-news
source: Dev.to
url: https://dev.to/ariless/waitforresponse-timing-the-one-line-fix-with-a-non-obvious-mental-model-89h
tags:
- tech-news
- dev.to
---

## waitForResponse() timing: the one-line fix with a non-obvious mental model

**Source**: Dev.to

  The test hung for 30 seconds. The response had already fired. One moved line fixed it.  

 The test hung for 30 seconds, then timed out. 

 The browser had received the response. The page had loaded. The data was there. 

 The test was still waiting. 




 
  
  
  The wizard
 

 I was writing a helper to walk through a 4-step booking wizard. After clicking "Next" on step 1, the page does a full navigation —  window.location.href  to step 2. Step 2 immediately loads doctor data from the API. 


**Lien**: [Lire](https://dev.to/ariless/waitforresponse-timing-the-one-line-fix-with-a-non-obvious-mental-model-89h)
