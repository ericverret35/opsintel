---
layout: post
title: Stop building notifications per product — notify, one platform for email, Slack,
  LINE, and webhooks
date: '2026-09-23'
category: tech-news
source: Dev.to
url: https://dev.to/uehara/stop-building-notifications-per-product-notify-one-platform-for-email-slack-line-and-webhooks-368o
tags:
- tech-news
- dev.to
---

## Stop building notifications per product — notify, one platform for email, Slack, LINE, and webhooks

**Source**: Dev.to

 
  
  
  The short version
 

 
 What we built: a shared platform called  notify  that sends notifications to email, Slack, LINE, and webhooks (automated system-to-system notifications) through a single API. Our internal products no longer implement their own notification plumbing; they just use the SDK (Software Development Kit — the client library for calling the platform) and a per-project API key. 
 Why we built it: multiple products were each implementing email sending and Slack notificati

**Lien**: [Lire](https://dev.to/uehara/stop-building-notifications-per-product-notify-one-platform-for-email-slack-line-and-webhooks-368o)
