---
layout: post
title: Why JavaScript Should Mutate State Instead of Styles
date: '2026-09-08'
category: tech-news
source: Dev.to
url: https://dev.to/ortizfranklindev/why-javascript-should-mutate-state-instead-of-styles-m6g
tags:
- tech-news
- dev.to
---

## Why JavaScript Should Mutate State Instead of Styles

**Source**: Dev.to

  Also available in  Español   

 
  
  
  The Problem
 

 A dropdown needs to open. A modal needs to appear. A nav link needs to show which section the reader is currently in. 

 The blunt route is  element.style.display = 'block'  state and appearance decided in the same line, nothing left for CSS to own. Most experienced developers already avoid this. The more common pattern is a class instead:  classList.toggle('is-open') . That's a real improvement, and a real state abstraction CSS decides 

**Lien**: [Lire](https://dev.to/ortizfranklindev/why-javascript-should-mutate-state-instead-of-styles-m6g)
