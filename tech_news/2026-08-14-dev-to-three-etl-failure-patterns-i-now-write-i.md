---
layout: post
title: Three ETL failure patterns I now write into the output file, not just the logs
date: '2026-08-14'
category: tech-news
source: Dev.to
url: https://dev.to/morinaga/three-etl-failure-patterns-i-now-write-into-the-output-file-not-just-the-logs-4in0
tags:
- tech-news
- dev.to
---

## Three ETL failure patterns I now write into the output file, not just the logs

**Source**: Dev.to

 My Reddit scraper returned empty arrays for 71 days. Nothing broke visibly. The market-listening output file kept being written, kept being committed to git, kept looking like a healthy daily snapshot. Nobody caught it until the interpretation layer noticed that Reddit-sourced signals hadn't changed in two months. 

 The three patterns I added afterward are small. Combined, they mean that failure mode can't happen silently again — the artifact itself reports what went wrong, not just the runner

**Lien**: [Lire](https://dev.to/morinaga/three-etl-failure-patterns-i-now-write-into-the-output-file-not-just-the-logs-4in0)
