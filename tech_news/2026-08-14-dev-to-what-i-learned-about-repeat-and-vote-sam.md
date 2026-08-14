---
layout: post
title: What I learned about repeat-and-vote sampling for non-deterministic search
  results
date: '2026-08-14'
category: tech-news
source: Dev.to
url: https://dev.to/morinaga/what-i-learned-about-repeat-and-vote-sampling-for-non-deterministic-search-results-18d7
tags:
- tech-news
- dev.to
---

## What I learned about repeat-and-vote sampling for non-deterministic search results

**Source**: Dev.to

 Repeating a YouTube search query three times and keeping only results that appear in two or more of those fetches is more reliable than treating any single fetch as ground truth. The Jaccard similarity between two fetches of the same query — within a single minute — sits around 0.43–0.88. Today's run measured 0.447 for the "more steam reviews than" query. That means roughly half the video IDs flipped between fetches. A single fetch isn't a signal; it's a snapshot of one shuffled result. 

 I bu

**Lien**: [Lire](https://dev.to/morinaga/what-i-learned-about-repeat-and-vote-sampling-for-non-deterministic-search-results-18d7)
