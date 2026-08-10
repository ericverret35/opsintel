---
layout: post
title: Automatically Renewing Tailscale HTTPS Certificates on PiKVM
date: '2026-08-10'
category: tech-news
source: Dev.to
url: https://dev.to/vast-cow/automatically-renewing-tailscale-https-certificates-on-pikvm-58e9
tags:
- tech-news
- dev.to
---

## Automatically Renewing Tailscale HTTPS Certificates on PiKVM

**Source**: Dev.to

 It is appropriate to continue using 
 

 
   ssl_certificate   /etc/kvmd/nginx/ssl/server.crt  ; 
 ssl_certificate_key   /etc/kvmd/nginx/ssl/server.key  ; 
  

 



 in  /etc/kvmd/nginx/ssl.conf , with a systemd timer checking the certificate expiration and updating these two files only when necessary. 

 The official PiKVM documentation also describes placing the Tailscale certificate in  /etc/kvmd/nginx/ssl/server.{crt,key} , setting the group to  kvmd-nginx , and then restarting  kvmd-nginx 

**Lien**: [Lire](https://dev.to/vast-cow/automatically-renewing-tailscale-https-certificates-on-pikvm-58e9)
