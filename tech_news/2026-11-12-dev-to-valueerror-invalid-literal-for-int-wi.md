---
layout: post
title: 'ValueError: invalid literal for int() with base 10 (Fix)'
date: '2026-11-12'
category: tech-news
source: Dev.to
url: https://dev.to/primeemre/valueerror-invalid-literal-for-int-with-base-10-fix-207f
tags:
- tech-news
- dev.to
---

## ValueError: invalid literal for int() with base 10 (Fix)

**Source**: Dev.to

 Your script runs, then Python stops with this: 
 

 
  ValueError: invalid literal for int() with base 10: '3.50'
  

 



 You gave  int()  a string that doesn't look like a whole number. The end of the message shows the exact text Python choked on, in quotes. So the error already tells you what's wrong. Below are the six inputs that cause it most often, and how to fix each one. I ran every example on Python 3.11, 3.12 and 3.14. All three print the same message. 

 
  
  
  What the Error Mean

**Lien**: [Lire](https://dev.to/primeemre/valueerror-invalid-literal-for-int-with-base-10-fix-207f)
