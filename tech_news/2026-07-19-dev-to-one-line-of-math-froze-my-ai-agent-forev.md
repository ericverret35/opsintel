---
layout: post
title: One line of math froze my AI agent forever. The timeout watched and did nothing.
date: '2026-07-19'
category: tech-news
source: Dev.to
url: https://dev.to/himanshu_748/one-line-of-math-froze-my-ai-agent-forever-the-timeout-watched-and-did-nothing-2dma
tags:
- tech-news
- dev.to
---

## One line of math froze my AI agent forever. The timeout watched and did nothing.

**Source**: Dev.to

  This is my second entry for the DEV x Sentry Bug Smash challenge.  Entry #1 was a crash with a confusing error message . This one is the opposite and it is scarier: no crash, no message, no event. Just silence.  

 
  
  
  The bug that sends you nothing
 

 smolagents runs LLM-generated Python in a sandboxed executor with a timeout. Issue  #2473  claims that one line of model-generated math defeats it completely: 
 

 
   from   smolagents.local_python_executor   import   LocalPythonExecutor 

**Lien**: [Lire](https://dev.to/himanshu_748/one-line-of-math-froze-my-ai-agent-forever-the-timeout-watched-and-did-nothing-2dma)
