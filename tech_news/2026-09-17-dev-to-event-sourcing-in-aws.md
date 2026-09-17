---
layout: post
title: Event Sourcing in AWS
date: '2026-09-17'
category: tech-news
source: Dev.to
url: https://dev.to/kerryconvery/event-sourcing-in-aws-4d8
tags:
- tech-news
- dev.to
---

## Event Sourcing in AWS

**Source**: Dev.to

 Imagine that your team has been running a distributed event sourced architecture for many years and then one day you realised that you've been doing event souring wrong the whole time. 

 This is where we are at now. 
    

 As you can see, change events are published from a microservice directly to a notification service while at the same time the application state is written to a database. 

 The problems 

 
  The event and the application state are not written within the same transaction.  

**Lien**: [Lire](https://dev.to/kerryconvery/event-sourcing-in-aws-4d8)
