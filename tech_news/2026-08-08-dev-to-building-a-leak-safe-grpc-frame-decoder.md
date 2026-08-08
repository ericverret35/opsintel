---
layout: post
title: Building a Leak-Safe gRPC Frame Decoder on Reactor Netty
date: '2026-08-08'
category: tech-news
source: Dev.to
url: https://dev.to/qianwj/building-a-leak-safe-grpc-frame-decoder-on-reactor-netty-po7
tags:
- tech-news
- dev.to
---

## Building a Leak-Safe gRPC Frame Decoder on Reactor Netty

**Source**: Dev.to

 This is the second article in my  grpc-reactor  series. The  first article  explains why I chose to build the runtime directly on Reactor Netty and where its compatibility boundary sits. This article moves one layer down into the Stage 1 protocol implementation: the frame decoder that every RPC shape relies on. 

 gRPC protobuf messages are not written directly as raw bytes into HTTP/2 DATA frames. Every message starts with a five-byte envelope: 
 

 
  byte 0      bit 0 indicates compression; 

**Lien**: [Lire](https://dev.to/qianwj/building-a-leak-safe-grpc-frame-decoder-on-reactor-netty-po7)
