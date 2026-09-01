---
layout: post
title: Godot sprite blurry when moving? Diagnose the right layer first
date: '2026-09-01'
category: tech-news
source: Dev.to
url: https://dev.to/framesprite/godot-sprite-blurry-when-moving-diagnose-the-right-layer-first-36e
tags:
- tech-news
- dev.to
---

## Godot sprite blurry when moving? Diagnose the right layer first

**Source**: Dev.to

 A sprite that is blurry while standing still and a sprite that only shimmers while moving are usually suffering from different bugs. Treating both as “bad filtering” leads to hours of random import changes. 

 Here is the shortest diagnostic path I use for Godot 4 pixel art. 

 
  
  
  1. Freeze the scene before touching import settings
 

 Pause the character on a single frame and stop the camera. 

 
 
 Soft edges while everything is still  usually indicate texture filtering. 
 
 Sharp while

**Lien**: [Lire](https://dev.to/framesprite/godot-sprite-blurry-when-moving-diagnose-the-right-layer-first-36e)
