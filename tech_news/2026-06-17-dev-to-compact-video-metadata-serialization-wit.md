---
layout: post
title: Compact Video Metadata Serialization With Protobuf Across PHP Services
date: '2026-06-17'
category: tech-news
source: Dev.to
url: https://dev.to/ahmet_gedik778845/compact-video-metadata-serialization-with-protobuf-across-php-services-19lk
tags:
- tech-news
- dev.to
---

## Compact Video Metadata Serialization With Protobuf Across PHP Services

**Source**: Dev.to

 Every two hours our ingest worker pulls a few thousand trending videos from regional sources, normalizes them, and hands the result to three downstream consumers: a ranking service that scores virality, an edge cache warmer that runs on Cloudflare Workers, and a Python analytics job that builds the GDPR-safe aggregates we show on the public site. For a long time the glue between those services was JSON. It worked, until it didn't. A single video record — title, channel, region tags, view/like d

**Lien**: [Lire](https://dev.to/ahmet_gedik778845/compact-video-metadata-serialization-with-protobuf-across-php-services-19lk)
