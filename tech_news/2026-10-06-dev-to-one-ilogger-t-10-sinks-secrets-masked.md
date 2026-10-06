---
layout: post
title: 'One ILogger<T>, 10 sinks, secrets masked everywhere: LoggerHelper + HttpHelper
  for .NET (and a playground to try them)'
date: '2026-10-06'
category: tech-news
source: Dev.to
url: https://dev.to/alessandro_chiodo_d820969/one-ilogger-10-sinks-secrets-masked-everywhere-loggerhelper-httphelper-for-net-and-a-6k3
tags:
- tech-news
- dev.to
---

## One ILogger<T>, 10 sinks, secrets masked everywhere: LoggerHelper + HttpHelper for .NET (and a playground to try them)

**Source**: Dev.to

 Every .NET team I've worked with ends up with the same logging wish list: 

 
 errors to a database, everything to a file, critical stuff to Telegram or email; 
 a different minimum level for each destination; 
 passwords, tokens and card numbers never leaving the process in clear text; 
 one broken sink must not take the app down; 
 HTTP calls that retry, time out and log themselves without boilerplate. 
 

 With plain Serilog and  HttpClient  all of this is possible, but it is a lot of JSON, 

**Lien**: [Lire](https://dev.to/alessandro_chiodo_d820969/one-ilogger-10-sinks-secrets-masked-everywhere-loggerhelper-httphelper-for-net-and-a-6k3)
