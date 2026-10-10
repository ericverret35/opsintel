---
layout: post
title: You Added `will-change` to Fix the Jank. You Made It Worse.
date: '2026-10-10'
category: tech-news
source: Dev.to
url: https://dev.to/parsajiravand/you-added-will-change-to-fix-the-jank-you-made-it-worse-51eg
tags:
- tech-news
- dev.to
---

## You Added `will-change` to Fix the Jank. You Made It Worse.

**Source**: Dev.to

 Open DevTools on almost any site that's been "optimized" for animation and check the  Layers  panel. There's a decent chance half the card grid, the nav, a modal backdrop, and a few  div s nobody can explain are each sitting in their own compositor layer — because at some point, someone added  will-change: transform  to fix a stutter, and it never came back off. 

 The property does exactly what it promises, which is the whole problem. Set it on one element, right before that element animates, 

**Lien**: [Lire](https://dev.to/parsajiravand/you-added-will-change-to-fix-the-jank-you-made-it-worse-51eg)
