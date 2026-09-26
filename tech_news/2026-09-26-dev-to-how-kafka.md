---
layout: post
title: How Kafka
date: '2026-09-26'
category: tech-news
source: Dev.to
url: https://dev.to/darshan_turakhia/how-kafka-2obk
tags:
- tech-news
- dev.to
---

## How Kafka

**Source**: Dev.to

 
 03:14 UTC. Security's on-call channel gets a message from the fraud-scanning job: a customer API key flagged and revoked four days earlier is still authorizing requests, all of them from ap-south-1. The revoke ticket has been closed as resolved since Monday. 
 




 
  
  
  the setup
 

  authz-gateway  sits in front of every API route and checks incoming keys against a local cache before anything touches the database. It used to call Postgres on every request; that was a flat 40ms added to 

**Lien**: [Lire](https://dev.to/darshan_turakhia/how-kafka-2obk)
