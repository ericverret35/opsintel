---
layout: post
title: 'Shipping one Flutter codebase to 6 platforms: what I learned building Tuneline'
date: '2026-06-21'
category: tech-news
source: Dev.to
url: https://dev.to/shamir_shakir_e293eb37a32/shipping-one-flutter-codebase-to-6-platforms-what-i-learned-building-tuneline-4jp8
tags:
- tech-news
- dev.to
---

## Shipping one Flutter codebase to 6 platforms: what I learned building Tuneline

**Source**: Dev.to

 I spent the last several months solo-building  Tuneline , a cross-platform media player, from a single Flutter codebase that ships native apps to  macOS, Windows, Linux, Android, Google TV, and iOS . No Electron. Here is the stack and a few things that bit me. 

 
  
  
  The stack
 

 
 
 Flutter 3.38 / Dart 3.10  — one codebase, six targets. 
 
 media_kit  for playback — libmpv on desktop, ExoPlayer on Android. Avoiding per-platform video plugins was the single biggest sanity win. 
 
 Riverpo

**Lien**: [Lire](https://dev.to/shamir_shakir_e293eb37a32/shipping-one-flutter-codebase-to-6-platforms-what-i-learned-building-tuneline-4jp8)
