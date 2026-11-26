---
layout: post
title: 'Analyzing Wireshark Captures: A Developer''s Guide to Reading the Wire'
date: '2026-11-26'
category: tech-news
source: Dev.to
url: https://dev.to/mango7777/analyzing-wireshark-captures-a-developers-guide-to-reading-the-wire-3i5p
tags:
- tech-news
- dev.to
---

## Analyzing Wireshark Captures: A Developer's Guide to Reading the Wire

**Source**: Dev.to

 The bug was a 200ms latency spike in our API that happened only in production. Logs showed nothing. APM showed nothing. We were about to add  time.Sleep(200 * time.Millisecond)  to a test to "make it deterministic" when someone suggested capturing the traffic. Five minutes with tcpdump and ten minutes with Wireshark later, we found it: a TCP retransmission caused by an MTU mismatch between our k8s pod and the NAT gateway. The packet was being sent, dropped, sent again, and the second one made i

**Lien**: [Lire](https://dev.to/mango7777/analyzing-wireshark-captures-a-developers-guide-to-reading-the-wire-3i5p)
