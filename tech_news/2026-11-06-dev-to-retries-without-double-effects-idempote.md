---
layout: post
title: 'Retries Without Double Effects: Idempotency Keys for LLM Tool Calls'
date: '2026-11-06'
category: tech-news
source: Dev.to
url: https://dev.to/obligra/retries-without-double-effects-idempotency-keys-for-llm-tool-calls-1hib
tags:
- tech-news
- dev.to
---

## Retries Without Double Effects: Idempotency Keys for LLM Tool Calls

**Source**: Dev.to

 An LLM agent decides to call your  create_refund  tool. The request times out. The agent framework retries, or the model simply asks for the same tool call again on its next turn. Did the customer get one refund or two? 

 Timeouts don't tell you whether the first attempt ran. That was true for every HTTP client long before LLMs, and the fix is the same: make the side-effecting operation idempotent, so repeating it is safe. What changes with agents is how often the repeat happens and how hard i

**Lien**: [Lire](https://dev.to/obligra/retries-without-double-effects-idempotency-keys-for-llm-tool-calls-1hib)
