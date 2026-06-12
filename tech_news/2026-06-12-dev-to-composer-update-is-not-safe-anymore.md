---
layout: post
title: Composer Update Is Not Safe Anymore
date: '2026-06-12'
category: tech-news
source: Dev.to
url: https://dev.to/tegos/composer-update-is-not-safe-anymore-2bcf
tags:
- tech-news
- dev.to
---

## Composer Update Is Not Safe Anymore

**Source**: Dev.to

 Saturday morning. I opened Twitter and saw a tweet about the Laravel-Lang packages being compromised. 

 My first reaction was simple: "I don't use that package." 

 Then I opened  composer.json  on a project I work on and found this in  require-dev : 
 

 
   "laravel-lang/lang"  :     "^14.8"  ,  
  "laravel-lang/publisher"  :     "^16.8"  ,  
   

 



 That changed things. 

 
  
  
  What Actually Happened
 

 The attack used  laravel-lang  packages as the distribution channel. And the sne

**Lien**: [Lire](https://dev.to/tegos/composer-update-is-not-safe-anymore-2bcf)
