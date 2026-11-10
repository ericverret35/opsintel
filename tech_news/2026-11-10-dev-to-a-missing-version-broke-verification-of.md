---
layout: post
title: A missing version broke verification of signed ARD search results
date: '2026-11-10'
category: tech-news
source: Dev.to
url: https://dev.to/alexar76/we-added-ard-discovery-to-six-hubs-and-found-a-broken-signed-search-result-3nlp
tags:
- tech-news
- dev.to
---

## A missing version broke verification of signed ARD search results

**Source**: Dev.to

 The weather result on modelmarket.dev looked complete until the verifier compared it with its signed subject. The subject named a version; the search result did not. 

 The full catalog entry had  version . A serializer had dropped it from the search representation while keeping the  trustManifest  that signed it. We caught that on November 4, during an ARD rollout to six AIMarket hubs, and deployed a second build. 

 The useful part of this bug is where it failed. Checking a signature and chec

**Lien**: [Lire](https://dev.to/alexar76/we-added-ard-discovery-to-six-hubs-and-found-a-broken-signed-search-result-3nlp)
