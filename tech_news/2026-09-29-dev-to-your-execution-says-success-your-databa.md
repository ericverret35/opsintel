---
layout: post
title: Your execution says success. Your database says nothing changed. Which one
  do you believe?
date: '2026-09-29'
category: tech-news
source: Dev.to
url: https://dev.to/aditya_mishra_2417/your-execution-says-success-your-database-says-nothing-changed-which-one-do-you-believe-1p1i
tags:
- tech-news
- dev.to
---

## Your execution says success. Your database says nothing changed. Which one do you believe?

**Source**: Dev.to

 Three threads here this month have circled the same gap: a green execution over work that never happened. The answers are all correct and all the same shape — RETURNING id, an If node, throw. Wire it per step, per workflow. 

 I got tired of wiring it per step, so I built the version that runs once. 

 What it does 

 Takes what the run claimed — "email sent", "order updated" — and goes and reads the authoritative system. Not the execution record, which the run wrote itself. The actual mailbox.

**Lien**: [Lire](https://dev.to/aditya_mishra_2417/your-execution-says-success-your-database-says-nothing-changed-which-one-do-you-believe-1p1i)
