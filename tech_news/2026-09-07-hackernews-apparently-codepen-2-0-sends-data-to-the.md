---
layout: post
title: Apparently CodePen 2.0 sends data to their servers as you type
date: '2026-09-07'
category: tech-news
source: HackerNews
url: https://news.ycombinator.com/item?id=49596976
tags:
- tech-news
- hackernews
---

## Apparently CodePen 2.0 sends data to their servers as you type

**Source**: HackerNews

 They send all typed into editor input to codepen.dev almost immediately (you would see in 1-2 sec after you typed your secret that it appears in respective Network/Response tab) even before one saved it. I tested this with a unique marker: after typing it into index.html, CodePen ran a build with "save:false", and the marker then appeared verbatim in the HTML served from the generated "*.codepen.dev preview". Thus, if you ever entered some secrets in there by mistake consider them compromized e

**Lien**: [Lire](https://news.ycombinator.com/item?id=49596976)
