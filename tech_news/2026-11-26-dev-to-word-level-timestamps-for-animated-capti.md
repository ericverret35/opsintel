---
layout: post
title: 'Word-Level Timestamps for Animated Captions: Parakeet vs Whisper on a CPU
  Server'
date: '2026-11-26'
category: tech-news
source: Dev.to
url: https://dev.to/imohgenius/word-level-timestamps-for-animated-captions-parakeet-vs-whisper-on-a-cpu-server-42l7
tags:
- tech-news
- dev.to
---

## Word-Level Timestamps for Animated Captions: Parakeet vs Whisper on a CPU Server

**Source**: Dev.to

 I'm building  AutoCaptions , a tool that adds animated, word-by-word captions to short videos. Everything starts with one requirement: a start time for every word. Sentence-level timing is fine for subtitles, but a word can't light up on cue if you don't know when it was said. 

 The constraint was cost. Transcription runs on a single ARM server with no GPU, shared with other sites. Here's what I tried and what I ended up shipping. 

 
  
  
  The benchmark
 

 I benchmarked a handful of open m

**Lien**: [Lire](https://dev.to/imohgenius/word-level-timestamps-for-animated-captions-parakeet-vs-whisper-on-a-cpu-server-42l7)
