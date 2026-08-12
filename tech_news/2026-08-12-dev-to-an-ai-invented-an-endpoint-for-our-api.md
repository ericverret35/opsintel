---
layout: post
title: An AI invented an endpoint for our API. We shipped it.
date: '2026-08-12'
category: tech-news
source: Dev.to
url: https://dev.to/jaweii/an-ai-invented-an-endpoint-for-our-api-we-shipped-it-4mo
tags:
- tech-news
- dev.to
---

## An AI invented an endpoint for our API. We shipped it.

**Source**: Dev.to

 A user sent us a bug report that was really a screenshot of someone else's chat. 
They had asked an AI assistant to build a web page that erases text from an 
image using our API, and it produced a complete, confident little demo: file 
input, preview pane, fetch call, error handling. It did not work. The error it 
reported was CORS. 

 It was not CORS. 
 
  
  
  What the model got wrong
 


 
   POST https://erasetext.com/api/mcp/erase
Authorization: Bearer et_…
FormData: image = &lt;File&gt;

**Lien**: [Lire](https://dev.to/jaweii/an-ai-invented-an-endpoint-for-our-api-we-shipped-it-4mo)
