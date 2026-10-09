---
layout: post
title: 'Nodemailer + Gmail errors, reproduced: 535-5.7.8, “Missing credentials for
  PLAIN”, wrong version number, and serverless ports'
date: '2026-10-09'
category: tech-news
source: Dev.to
url: https://dev.to/formgongteam/nodemailer-gmail-errors-reproduced-535-578-missing-credentials-for-plain-wrong-version-2fp7
tags:
- tech-news
- dev.to
---

## Nodemailer + Gmail errors, reproduced: 535-5.7.8, “Missing credentials for PLAIN”, wrong version number, and serverless ports

**Source**: Dev.to

 A contact form that sends through Gmail with Nodemailer usually fails in one of a handful of ways, and the error text often points in the wrong direction. We reproduced each failure against the real  smtp.gmail.com  on 9 October 2026, with Nodemailer 10.0.16 on Node and a made-up Gmail address, so every attempt failed before a message could be accepted. Then we ran the same code on Cloudflare Workers. 

 What we learned in short: 

 
 
  Missing credentials for "PLAIN"  never reached Google.  N

**Lien**: [Lire](https://dev.to/formgongteam/nodemailer-gmail-errors-reproduced-535-578-missing-credentials-for-plain-wrong-version-2fp7)
