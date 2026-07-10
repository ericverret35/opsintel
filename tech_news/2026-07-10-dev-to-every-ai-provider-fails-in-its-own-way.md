---
layout: post
title: Every AI provider fails in its own way. I stopped checking status codes and
  built an error model instead.
date: '2026-07-10'
category: tech-news
source: Dev.to
url: https://dev.to/manolito99/every-ai-provider-fails-in-its-own-way-i-stopped-checking-status-codes-and-built-an-error-model-25do
tags:
- tech-news
- dev.to
---

## Every AI provider fails in its own way. I stopped checking status codes and built an error model instead.

**Source**: Dev.to

 I built an API gateway that routes between OpenAI, Anthropic and Gemini. I figured integrating both providers would be the hard part. 

 It wasn't. Calling their APIs is maybe an afternoon of work each. The hard part showed up later, the first time something went wrong. 

 
  
  
  The moment it broke
 

 Early on, my error handling was basically: catch whatever the provider throws, forward the status code, move on. 
 

 
   }   catch   (  error  )   { 
   res  .  status  (  error  .  status   

**Lien**: [Lire](https://dev.to/manolito99/every-ai-provider-fails-in-its-own-way-i-stopped-checking-status-codes-and-built-an-error-model-25do)
