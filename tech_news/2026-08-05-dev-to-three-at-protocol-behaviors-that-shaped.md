---
layout: post
title: Three AT Protocol behaviors that shaped my Bluesky post queue design
date: '2026-08-05'
category: tech-news
source: Dev.to
url: https://dev.to/morinaga/three-at-protocol-behaviors-that-shaped-my-bluesky-post-queue-design-3h30
tags:
- tech-news
- dev.to
---

## Three AT Protocol behaviors that shaped my Bluesky post queue design

**Source**: Dev.to

 Three behaviors stopped me from shipping my first Bluesky post queue correctly. None of them are prominently surfaced in the  AT Protocol lexicon documentation  in a form that would have helped me avoid them. I found all three by reading failed requests in CI logs. 

 
  
  
  Rate limits reset on a rolling 24-hour window, not at midnight
 

 The AT Protocol enforces rate limits per session token. The primary limit for a posting bot on app.bsky.social is 1,666 create operations per hour. What t

**Lien**: [Lire](https://dev.to/morinaga/three-at-protocol-behaviors-that-shaped-my-bluesky-post-queue-design-3h30)
