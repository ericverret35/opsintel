---
layout: post
title: 'The TODO shipped to npm: an unauthenticated route that could stop any city''s
  AI workflow (Your Priorities, @yrpri/api < 9.0.244)'
date: '2026-09-02'
category: tech-news
source: Dev.to
url: https://dev.to/santosh_kumarpuppala_96e/the-todo-shipped-to-npm-an-unauthenticated-route-that-could-stop-any-citys-ai-workflow-your-pkd
tags:
- tech-news
- dev.to
---

## The TODO shipped to npm: an unauthenticated route that could stop any city's AI workflow (Your Priorities, @yrpri/api < 9.0.244)

**Source**: Dev.to

 
  
  
  TL;DR
 

 
 
 What:  In Your Priorities — the Citizens Foundation's open-source participatory-democracy platform, the one municipalities self-host to run citizen deliberation — two Express routes in the AI-assistant controller were registered with  no authorization middleware at all , directly beneath a comment reading  //TODO: Add auth for below . The handler for  PUT /api/assistants/:groupId/:agentId/:runId/advanceOrStopWorkflow  resolved the target run by bare primary key and never 

**Lien**: [Lire](https://dev.to/santosh_kumarpuppala_96e/the-todo-shipped-to-npm-an-unauthenticated-route-that-could-stop-any-citys-ai-workflow-your-pkd)
