---
layout: post
title: Our AI assistant can write to exactly one table. Postgres enforces it, not
  our code
date: '2026-11-14'
category: tech-news
source: Dev.to
url: https://dev.to/appwebseo/our-ai-assistant-can-write-to-exactly-one-table-postgres-enforces-it-not-our-code-4pp7
tags:
- tech-news
- dev.to
---

## Our AI assistant can write to exactly one table. Postgres enforces it, not our code

**Source**: Dev.to

 We build  Reperline , a small system that tracks construction schedules, budgets and contracts. It also connects to Claude through MCP (Model Context Protocol), so a project manager can ask "which milestones are late?" or upload an invoice and have Claude prepare the entry. 

 That second part is where it gets uncomfortable. Budget data is money. We did not want "the AI only proposes changes" to be a promise made by application code that one refactor could break. We wanted the database to make 

**Lien**: [Lire](https://dev.to/appwebseo/our-ai-assistant-can-write-to-exactly-one-table-postgres-enforces-it-not-our-code-4pp7)
