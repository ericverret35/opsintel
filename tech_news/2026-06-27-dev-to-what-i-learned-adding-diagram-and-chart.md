---
layout: post
title: What I learned adding diagram and chart slides to a CI-rendered YouTube pipeline
date: '2026-06-27'
category: tech-news
source: Dev.to
url: https://dev.to/morinaga/what-i-learned-adding-diagram-and-chart-slides-to-a-ci-rendered-youtube-pipeline-3bnl
tags:
- tech-news
- dev.to
---

## What I learned adding diagram and chart slides to a CI-rendered YouTube pipeline

**Source**: Dev.to

 The conclusion first: pre-rendering diagrams and charts to PNG before compositing them onto slides — rather than generating visual content inline or inside ffmpeg — is the right architecture for a CI video pipeline. The tooling gap between Chromium-backed Mermaid rendering, headless matplotlib, and ffmpeg's static frame expectation makes a shared PNG handoff the only approach that keeps each piece testable and replaceable. 

 I added three new slide types to the  YouTube slide renderer  last we

**Lien**: [Lire](https://dev.to/morinaga/what-i-learned-adding-diagram-and-chart-slides-to-a-ci-rendered-youtube-pipeline-3bnl)
