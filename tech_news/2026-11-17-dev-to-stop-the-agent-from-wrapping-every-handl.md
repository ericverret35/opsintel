---
layout: post
title: Stop the agent from wrapping every handler in useMemo “for performance”
date: '2026-11-17'
category: tech-news
source: Dev.to
url: https://dev.to/sherotree/stop-the-agent-from-wrapping-every-handler-in-usememo-for-performance-3h81
tags:
- tech-news
- dev.to
---

## Stop the agent from wrapping every handler in useMemo “for performance”

**Source**: Dev.to

 The PR “cleans up” a form by wrapping every event handler in  useCallback  and every derived boolean in  useMemo . The commit message says “performance.” There is no profile, no skipped render that mattered, and two stale-closure bugs in the validation path. 

 I’ve started treating  agent-added  useMemo  /  useCallback  without a stated reason as noise , not as an optimization. React is not cheaper just because the call site looks official. The wrappers are extra dependencies to get wrong. 

 

**Lien**: [Lire](https://dev.to/sherotree/stop-the-agent-from-wrapping-every-handler-in-usememo-for-performance-3h81)
