---
layout: post
title: Connecting a Netlify Function to a Home Server via a Cloudflare Tunnel
date: '2026-10-11'
category: tech-news
source: Dev.to
url: https://dev.to/the_bomber_f1e42beb1feaec/connecting-a-netlify-function-to-a-home-server-via-a-cloudflare-tunnel-418n
tags:
- tech-news
- dev.to
---

## Connecting a Netlify Function to a Home Server via a Cloudflare Tunnel

**Source**: Dev.to

 
  
  
  Why I needed a tunnel
 

 I run a small home automation server on my personal network. It hosts a few Node.js services that expose a JSON API for my smart lights, a webhook endpoint for a contact form, and a simple status page. I wanted to call those endpoints from a Netlify site without exposing my home IP directly. Cloudflare's  quick tunnel  (formerly Argo Tunnel) gives me a public HTTPS URL that forwards traffic to a local port, but the URL changes each time the tunnel restarts. Th

**Lien**: [Lire](https://dev.to/the_bomber_f1e42beb1feaec/connecting-a-netlify-function-to-a-home-server-via-a-cloudflare-tunnel-418n)
