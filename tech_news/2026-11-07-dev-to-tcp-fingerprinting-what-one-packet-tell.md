---
layout: post
title: 'TCP Fingerprinting: What One Packet Tells a Server About Your OS'
date: '2026-11-07'
category: tech-news
source: Dev.to
url: https://dev.to/parallaxgrain/tcp-fingerprinting-what-one-packet-tells-a-server-about-your-os-4ofa
tags:
- tech-news
- dev.to
---

## TCP Fingerprinting: What One Packet Tells a Server About Your OS

**Source**: Dev.to

 A web server learns something about your machine before it parses a single header. The SYN packet that opens every TCP connection carries a hop budget, a window size, a segment size and a list of options, and your operating system picked all of them. TCP fingerprinting reads those values and guesses the OS behind the connection. It needs no JavaScript and no cookies, and the visitor never sees it happen. 

 
 A browser can claim any operating system. The first packet shows what the kernel behin

**Lien**: [Lire](https://dev.to/parallaxgrain/tcp-fingerprinting-what-one-packet-tells-a-server-about-your-os-4ofa)
