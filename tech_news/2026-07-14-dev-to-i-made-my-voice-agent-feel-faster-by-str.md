---
layout: post
title: I Made My Voice Agent Feel Faster by Streaming Sentences, Not Audio
date: '2026-07-14'
category: tech-news
source: Dev.to
url: https://dev.to/toddsullivan/i-made-my-voice-agent-feel-faster-by-streaming-sentences-not-audio-4jej
tags:
- tech-news
- dev.to
---

## I Made My Voice Agent Feel Faster by Streaming Sentences, Not Audio

**Source**: Dev.to

 The annoying thing about voice agents is that “the model is fast” does not mean the experience is fast. 

 I had a small voice assistant running on a local device, talking to a hosted chat backend. The actual LLM call was only one part of the wait. The full path looked more like this: 

 
 wake word detection 
 speech recognition 
 authenticated  /chat  call 
 model response 
 local TTS synthesis 
 audio playback 
 

 If you wait for step 4 to finish before starting step 5, the user hears nothi

**Lien**: [Lire](https://dev.to/toddsullivan/i-made-my-voice-agent-feel-faster-by-streaming-sentences-not-audio-4jej)
