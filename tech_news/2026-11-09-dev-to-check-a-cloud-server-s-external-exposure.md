---
layout: post
title: Check a cloud server's external exposure in one command
date: '2026-11-09'
category: tech-news
source: Dev.to
url: https://dev.to/tuxxin/check-a-cloud-servers-external-exposure-in-one-command-29m1
tags:
- tech-news
- dev.to
---

## Check a cloud server's external exposure in one command

**Source**: Dev.to

 Run  curl -4 https://qsa.sh  on the cloud server. qsa.sh prints the public IPv4 address your request came from, waits 15 seconds, then scans that address from its own scanner network and streams back three things: the open TCP ports, the service and version on each port with known CVE matches, and nuclei findings. Put that list next to your security group or firewall rules and every difference between the two is a configuration you need to look at. 

 
  
  
  Run the scan from the server
 





**Lien**: [Lire](https://dev.to/tuxxin/check-a-cloud-servers-external-exposure-in-one-command-29m1)
