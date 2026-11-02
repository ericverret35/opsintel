---
layout: post
title: Find a Brute-Force Attack in auth.log With grep, awk and sort
date: '2026-11-02'
category: tech-news
source: Dev.to
url: https://dev.to/seanofodile/find-a-brute-force-attack-in-authlog-with-grep-awk-and-sort-3e0n
tags:
- tech-news
- dev.to
---

## Find a Brute-Force Attack in auth.log With grep, awk and sort

**Source**: Dev.to

 Your server is on the internet, so someone is guessing SSH passwords right now. Here's how to see it, measure it and respond, using only standard tools. You can practise every command safely in the free browser lab on  CoreQ Academy . 

 
  
  
  1. Look at the evidence
 

 On Debian and Ubuntu, SSH authentication events go to  /var/log/auth.log  (on RHEL-family systems,  /var/log/secure ). You need root or membership in the  adm  group to read it. 
 

 
   sudo tail   -n  20 /var/log/auth.log


**Lien**: [Lire](https://dev.to/seanofodile/find-a-brute-force-attack-in-authlog-with-grep-awk-and-sort-3e0n)
