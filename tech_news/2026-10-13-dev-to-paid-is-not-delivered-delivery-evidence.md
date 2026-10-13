---
layout: post
title: 'Paid Is Not Delivered: Delivery Evidence for an x402 API on a Cloudflare Worker'
date: '2026-10-13'
category: tech-news
source: Dev.to
url: https://dev.to/noboru/paid-is-not-delivered-delivery-evidence-for-an-x402-api-on-a-cloudflare-worker-3pf0
tags:
- tech-news
- dev.to
---

## Paid Is Not Delivered: Delivery Evidence for an x402 API on a Cloudflare Worker

**Source**: Dev.to

 I run a small paid HTTP API on a Cloudflare Worker:  x402-catalog-history , priced in USDC on Base with the x402  exact  scheme. This post is not about the product. It is about one narrow problem that caused me more confusion than the payment integration itself:  knowing whether a buyer who paid actually received the response.  Every number below comes from my own deployment logs and test runs; anything unmeasured is marked as unverified. 

 
  
  
  1. What the service is
 

 
 Cloudflare Work

**Lien**: [Lire](https://dev.to/noboru/paid-is-not-delivered-delivery-evidence-for-an-x402-api-on-a-cloudflare-worker-3pf0)
