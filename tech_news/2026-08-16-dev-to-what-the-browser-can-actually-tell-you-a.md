---
layout: post
title: What the browser can actually tell you about your hardware (and what it can't)
date: '2026-08-16'
category: tech-news
source: Dev.to
url: https://dev.to/member_2ef2ebd8/what-the-browser-can-actually-tell-you-about-your-hardware-and-what-it-cant-2d2j
tags:
- tech-news
- dev.to
---

## What the browser can actually tell you about your hardware (and what it can't)

**Source**: Dev.to

 I spent a while building browser-based hardware diagnostics and came away with a much clearer sense of where the web platform is genuinely capable and where it quietly lies to you. Notes below, with live demos for each API so you can poke at them yourself. 

 
  
  
  Refresh rate:  requestAnimationFrame  is the only signal you get
 

 There's no  screen.refreshRate . The only approach is timing  requestAnimationFrame  callbacks and inferring the rate from the median frame delta: 
 

 
   const

**Lien**: [Lire](https://dev.to/member_2ef2ebd8/what-the-browser-can-actually-tell-you-about-your-hardware-and-what-it-cant-2d2j)
