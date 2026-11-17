---
layout: post
title: Test Debezium CDC Pipelines with Sandboxes
date: '2026-11-17'
category: tech-news
source: Dev.to
url: https://dev.to/signadot/test-debezium-cdc-pipelines-with-sandboxes-54og
tags:
- tech-news
- dev.to
---

## Test Debezium CDC Pipelines with Sandboxes

**Source**: Dev.to

  Read this tutorial on  Signadot docs .  

  Sandboxes  route a request to the right version of a service by its  routing key , which travels in request headers. Change data capture breaks that chain twice. The service that handles the request only writes a row, and  Debezium  publishes the event later from the database's write-ahead log, without ever seeing the request. 

 This tutorial shows how to get the routing key through anyway. An  orders  service writes orders to Postgres, Debezium pub

**Lien**: [Lire](https://dev.to/signadot/test-debezium-cdc-pipelines-with-sandboxes-54og)
