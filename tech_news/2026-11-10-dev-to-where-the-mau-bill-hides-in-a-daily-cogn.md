---
layout: post
title: Where the MAU Bill Hides in a Daily Cognito Audit Job
date: '2026-11-10'
category: tech-news
source: Dev.to
url: https://dev.to/rafagross/where-the-mau-bill-hides-in-a-daily-cognito-audit-job-1ojl
tags:
- tech-news
- dev.to
---

## Where the MAU Bill Hides in a Daily Cognito Audit Job

**Source**: Dev.to

 I'm designing a multi-tenant SaaS that keeps every customer in a single Cognito user pool. Self sign-up is off. Accounts are created by an operator path, each customer has around 200 users, and administrators must use TOTP. 

 One of the jobs in the plan runs once a day and reconciles two things: email addresses that changed outside the expected flow, and administrators who don't have TOTP set up. It's a small security control. It is also, written the obvious way, a line on the bill that grows 

**Lien**: [Lire](https://dev.to/rafagross/where-the-mau-bill-hides-in-a-daily-cognito-audit-job-1ojl)
