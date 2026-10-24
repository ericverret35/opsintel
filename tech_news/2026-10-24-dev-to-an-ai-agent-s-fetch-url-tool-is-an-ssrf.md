---
layout: post
title: 'An AI Agent''s fetch(url) Tool Is an SSRF Surface: Controls That Do Not Rely
  on the Model'
date: '2026-10-24'
category: tech-news
source: Dev.to
url: https://dev.to/ookeolioli222/an-ai-agents-fetchurl-tool-is-an-ssrf-surface-controls-that-do-not-rely-on-the-model-26eb
tags:
- tech-news
- dev.to
---

## An AI Agent's fetch(url) Tool Is an SSRF Surface: Controls That Do Not Rely on the Model

**Source**: Dev.to

 A tool that takes a URL and returns the page is one of the most common additions to an AI agent. It is also a server-side request whose destination is chosen by a model, and the model reads content that someone else wrote: web pages, support tickets, documents, e-mail. When that content says "fetch this address next", the request leaves from the server's network position, not from the author's. 

 The question for a review is not "can the model be made to behave". It is "what can this tool reac

**Lien**: [Lire](https://dev.to/ookeolioli222/an-ai-agents-fetchurl-tool-is-an-ssrf-surface-controls-that-do-not-rely-on-the-model-26eb)
