---
layout: post
title: Shipping Stock CLIs as Subprocess Instead of Static-Linking SDKs
date: '2026-08-23'
category: tech-news
source: Dev.to
url: https://dev.to/jearry/shipping-stock-clis-as-subprocess-instead-of-static-linking-sdks-1jl8
tags:
- tech-news
- dev.to
---

## Shipping Stock CLIs as Subprocess Instead of Static-Linking SDKs

**Source**: Dev.to

 I'm building yyzTools, which bundles 9 third-party engines (OpenSSL, FFmpeg, ImageMagick, pdfcpu, Aria2, 7-Zip, RapidOCR, Everything...). I chose to spawn them as subprocesses rather than static-link their SDKs. Here's why—and the cost. 

 The conventional approach 
When your app needs OpenSSL crypto, FFmpeg video processing, ImageMagick image ops—you reach for the SDK. Link libssl, link libav*, link libMagick. One binary, no external deps, fast function calls. It's the textbook answer. 

 I di

**Lien**: [Lire](https://dev.to/jearry/shipping-stock-clis-as-subprocess-instead-of-static-linking-sdks-1jl8)
