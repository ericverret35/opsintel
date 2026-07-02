---
layout: post
title: The commands section is the highest-ROI part of your AGENTS.md
date: '2026-07-02'
category: tech-news
source: Dev.to
url: https://dev.to/promptmaster/the-commands-section-is-the-highest-roi-part-of-your-agentsmd-k5j
tags:
- tech-news
- dev.to
---

## The commands section is the highest-ROI part of your AGENTS.md

**Source**: Dev.to

 
  
  
  Why commands matter most
 

 Most agent tasks end in a build or a test. List the  exact  commands and the agent runs them, reads the output, and fixes its own errors before finishing. Leave them out and it guesses — or reports success on code that never passed. 

 
  
  
  Be literal
 

 "Run the tests" can't be executed.  pnpm test  can. 
 

 
   ## Commands 
Install:    pnpm install --frozen-lockfile
Dev:        pnpm dev
Build:      pnpm build
Test (all): pnpm test
Test (one): pnpm t

**Lien**: [Lire](https://dev.to/promptmaster/the-commands-section-is-the-highest-roi-part-of-your-agentsmd-k5j)
