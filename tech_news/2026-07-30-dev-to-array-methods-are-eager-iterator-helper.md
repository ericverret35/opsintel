---
layout: post
title: Array methods are eager. Iterator helpers are lazy. Here's why that matters.
date: '2026-07-30'
category: tech-news
source: Dev.to
url: https://dev.to/parsajiravand/array-methods-are-eager-iterator-helpers-are-lazy-heres-why-that-matters-58li
tags:
- tech-news
- dev.to
---

## Array methods are eager. Iterator helpers are lazy. Here's why that matters.

**Source**: Dev.to

 Every time you chain  .filter()  and  .map()  on an array, JavaScript creates two new arrays. For small lists this is invisible. For a large dataset, a generator producing values on demand, or a stream where you only need the first handful of results, you've materialized thousands of elements you immediately discard. 

 Iterator helpers are the lazy alternative. They shipped natively in Chrome 122, Firefox 131, and Safari 18.2 — no library, no polyfill, no build step. 

 
  
  
  What "lazy" me

**Lien**: [Lire](https://dev.to/parsajiravand/array-methods-are-eager-iterator-helpers-are-lazy-heres-why-that-matters-58li)
