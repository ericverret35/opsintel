---
layout: post
title: 'From CSS selector to source line: instrumenting Angular templates'
date: '2026-08-23'
category: tech-news
source: Dev.to
url: https://dev.to/oussama_laribi_dad54a6441/from-css-selector-to-source-line-instrumenting-angular-templates-3oni
tags:
- tech-news
- dev.to
---

## From CSS selector to source line: instrumenting Angular templates

**Source**: Dev.to

 Every accessibility tool I have used reports violations like this: 
 

 
  Images must have alternative text
  body &gt; main &gt; div:nth-child(2) &gt; form &gt; div.field &gt; img
  

 



 That selector is correct. It is also useless. It describes the  rendered DOM , 
and I do not write rendered DOM — I write templates. Somewhere in a few hundred 
 .component.html  files there is an  &lt;img&gt;  that produced it, and finding it is 
manual work: grep for  img , get forty hits, open them one 

**Lien**: [Lire](https://dev.to/oussama_laribi_dad54a6441/from-css-selector-to-source-line-instrumenting-angular-templates-3oni)
