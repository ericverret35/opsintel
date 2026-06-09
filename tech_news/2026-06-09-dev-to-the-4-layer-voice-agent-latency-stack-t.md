---
layout: post
title: The 4-layer voice-agent latency stack, traced with OTel spans
date: '2026-06-09'
category: tech-news
source: Dev.to
url: https://dev.to/realmarcuschen/the-4-layer-voice-agent-latency-stack-traced-with-otel-spans-37hp
tags:
- tech-news
- dev.to
---

## The 4-layer voice-agent latency stack, traced with OTel spans

**Source**: Dev.to

 ** 

 
  
  
  How I instrument ASR, LLM, TTS, and the client with OpenTelemetry, and which number in each layer I actually look at
 

 ** 

  TL;DR.  A voice agent is four moving parts stuck together: speech to text, the model that writes the reply, text to speech, and the client that plays the audio back. End to end latency hides which of those four is slow on any given turn, so I stopped tracking it as one number and started tracing each stage as its own OTel span with a shared session id. T

**Lien**: [Lire](https://dev.to/realmarcuschen/the-4-layer-voice-agent-latency-stack-traced-with-otel-spans-37hp)
