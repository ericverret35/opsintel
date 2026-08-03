---
layout: post
title: 'Fail the build when your prompt gets dumber: evalgate for prompt regression
  CI'
date: '2026-08-03'
category: tech-news
source: Dev.to
url: https://dev.to/royalpinto007/fail-the-build-when-your-prompt-gets-dumber-evalgate-for-prompt-regression-ci-4k36
tags:
- tech-news
- dev.to
---

## Fail the build when your prompt gets dumber: evalgate for prompt regression CI

**Source**: Dev.to

 Prompts rot silently. I swap a model, tweak a system prompt, add a tool, and everything still runs. No exception is thrown, no test goes red, the JSON still parses. The output is just quietly worse, and I usually find out from a user rather than from CI. Unit tests are the wrong instrument here because there is nothing to catch: the failure mode is not a crash, it is a drop in quality. 

 So I built  evalgate , a small TypeScript tool that treats prompt and agent quality like a build artifact. 

**Lien**: [Lire](https://dev.to/royalpinto007/fail-the-build-when-your-prompt-gets-dumber-evalgate-for-prompt-regression-ci-4k36)
