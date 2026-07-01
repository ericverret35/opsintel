---
layout: post
title: Proxying RabbitMQ Management UI Through Nginx (Fixing the %2F Problem)
date: '2026-07-01'
category: tech-news
source: Dev.to
url: https://dev.to/aswindanu_anwar_38c31d278/proxying-rabbitmq-management-ui-through-nginx-fixing-the-2f-problem-3dj0
tags:
- tech-news
- dev.to
---

## Proxying RabbitMQ Management UI Through Nginx (Fixing the %2F Problem)

**Source**: Dev.to

 
  
  
  The Problem
 

 When you put RabbitMQ's Management UI behind an nginx reverse proxy under a 
sub-path like  /rabbitmq/ , queue detail pages and many API calls break silently. 

 The root cause: nginx normalizes the request URI before proxying. It decodes 
 %2F  (the URL-encoded forward slash) into a literal  / . RabbitMQ's Management 
API uses  %2F  to represent the  default virtual host  ( / ) in API paths: 

 
  GET /api/queues/%2F/my-queue
  

 

 When nginx decodes it: 

 
  GET /a

**Lien**: [Lire](https://dev.to/aswindanu_anwar_38c31d278/proxying-rabbitmq-management-ui-through-nginx-fixing-the-2f-problem-3dj0)
