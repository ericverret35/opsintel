---
layout: post
title: Our homepage serves 24 logo elements for 12 logo files, and four more files
  nobody has ever requested
date: '2026-11-01'
category: tech-news
source: Dev.to
url: https://dev.to/daniel_pertu/our-homepage-serves-24-logo-elements-for-12-logo-files-and-four-more-files-nobody-has-ever-3042
tags:
- tech-news
- dev.to
---

## Our homepage serves 24 logo elements for 12 logo files, and four more files nobody has ever requested

**Source**: Dev.to

 The  CogniPrep landing page  has a wall of company logos under the hero with the caption "Some companies that our clients have applied to". Twelve logos, three rows of four, about as simple as a component gets. 

 Here is what the deployed HTML actually contains: 
 

 
  curl  -s  https://cogniprep.app/ |  grep   -o   '&lt;img[^&gt;]*logos/[a-z-]*\.svg[^&gt;]*&gt;'  |  wc   -l 
  

 



 
 Every logo twice. 
 

 
  
  
  Why there are two of each
 

 The hero is a two-column layout on desktop w

**Lien**: [Lire](https://dev.to/daniel_pertu/our-homepage-serves-24-logo-elements-for-12-logo-files-and-four-more-files-nobody-has-ever-3042)
