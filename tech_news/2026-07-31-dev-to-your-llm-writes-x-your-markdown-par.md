---
layout: post
title: Your LLM Writes \(x\), Your Markdown Parser Wants $x$
date: '2026-07-31'
category: tech-news
source: Dev.to
url: https://dev.to/duz52/your-llm-writes-x-your-markdown-parser-wants-x-3n3l
tags:
- tech-news
- dev.to
---

## Your LLM Writes \(x\), Your Markdown Parser Wants $x$

**Source**: Dev.to

  TL;DR  — LLMs love  \(...\)  and  \[...\] . Most Markdown math plugins only speak  $...$  and  $$...$$ . I tried to bridge that with a regex, failed in interesting ways, and ended up teaching the tokenizer instead. Two packages came out of it:   micromark-extension-math-extended   and   remark-math-extended  . 




 
  
  
  The setup
 

 Sometimes the hard part of rendering math isn't the equation. It's agreeing on where the equation  starts and stops . 

 I was piping Markdown from some Open

**Lien**: [Lire](https://dev.to/duz52/your-llm-writes-x-your-markdown-parser-wants-x-3n3l)
