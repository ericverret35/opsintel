---
layout: post
title: Sending a frame (not a byte) is a Kafka API choice. WKafka makes it format="image"
date: '2026-09-26'
category: tech-news
source: Dev.to
url: https://dev.to/william_rodriguez_65a5898/sending-a-frame-not-a-byte-is-a-kafka-api-choice-wkafka-makes-it-formatimage-4pmn
tags:
- tech-news
- dev.to
---

## Sending a frame (not a byte) is a Kafka API choice. WKafka makes it format="image"

**Source**: Dev.to

 Kafka delivers bytes. It does not care if they are a contract, a cat photo or a satellite frame. For a team that streams vision data, "raw bytes" means every consumer re-implements decoding, shape-guessing and channel-order handling. WKafka's answer is a contract the library enforces: images are a first-class message. 

 
 Day 03 of the WKafka open-source series — decorator-based, MIT, reproducible. 
 

 
  
  
  What "image" means as a format
 

 Producer sends a NumPy array, not a blob: 
 

 

**Lien**: [Lire](https://dev.to/william_rodriguez_65a5898/sending-a-frame-not-a-byte-is-a-kafka-api-choice-wkafka-makes-it-formatimage-4pmn)
