---
layout: post
title: Versioning a Laravel REST API without making a mess
date: '2026-11-23'
category: tech-news
source: Dev.to
url: https://dev.to/arun_tyagi_developer/versioning-a-laravel-rest-api-without-making-a-mess-3kdc
tags:
- tech-news
- dev.to
---

## Versioning a Laravel REST API without making a mess

**Source**: Dev.to

 Your first API client ships, then the mobile app ships, then a partner integration ships, and suddenly you can't rename a single field. Versioning is how you keep moving without breaking people. 

 Here's the setup I use on client Laravel APIs. 

 
  
  
  1. Version in the URL, not headers
 

 Header-based versioning ( Accept: application/vnd.app.v2+json ) is elegant, but URL versioning ( /api/v1/... ) is easier to debug, cache, log and explain to a partner's developer. I default to the URL. 


**Lien**: [Lire](https://dev.to/arun_tyagi_developer/versioning-a-laravel-rest-api-without-making-a-mess-3kdc)
