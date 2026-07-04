---
layout: post
title: I built a static AI tools directory with 1,638 auto-generated pages — here's
  the full technical breakdown
date: '2026-07-04'
category: tech-news
source: Dev.to
url: https://dev.to/bhagvat_meena_9f123a2f2d5/i-built-a-static-ai-tools-directory-with-1638-auto-generated-pages-heres-the-full-technical-25m2
tags:
- tech-news
- dev.to
---

## I built a static AI tools directory with 1,638 auto-generated pages — here's the full technical breakdown

**Source**: Dev.to

 I've been building AsmiAI (asmiai.xyz) for the past 6 months — a fully static AI tools directory with 236 reviewed tools, 1,638 side-by-side comparison pages, and a free AI chat advisor. Zero database, zero framework, free hosting. 

 Here's exactly how it works technically. 

 
  
  
  The build system
 

 Everything is generated from JSON data files at build time using Node.js and Python. One  ./build-asmiai.sh  command generates 2,373 pages in under 2 minutes and deploys to Cloudflare Pages.

**Lien**: [Lire](https://dev.to/bhagvat_meena_9f123a2f2d5/i-built-a-static-ai-tools-directory-with-1638-auto-generated-pages-heres-the-full-technical-25m2)
