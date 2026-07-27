---
layout: post
title: How to achieve zero-copy streaming from hyper and h3-quinn into a Wasmtime
  Wasm component via wasi:http?
date: '2026-07-27'
category: tech-news
source: Dev.to
url: https://dev.to/josh_klein/how-to-achieve-zero-copy-streaming-from-hyper-and-h3-quinn-into-a-wasmtime-wasm-component-via-10hl
tags:
- tech-news
- dev.to
---

## How to achieve zero-copy streaming from hyper and h3-quinn into a Wasmtime Wasm component via wasi:http?

**Source**: Dev.to

 Hello everyone, 

 I am currently building a high-performance API gateway that integrates business logic components—implemented via WASI and running within Wasmtime—as HTTP/TCP/QUIC handlers. I am exploring the best design approach to achieve a zero-copy data path from the upstream network layer—specifically  hyper  for HTTP/1.x and HTTP/2, and  h3-quinn  (based on Quinn) for HTTP/3—to the  wasi:http  guest environment. 

 Given that: 

 hyper and h3-quinn each manage their own internal buffer 

**Lien**: [Lire](https://dev.to/josh_klein/how-to-achieve-zero-copy-streaming-from-hyper-and-h3-quinn-into-a-wasmtime-wasm-component-via-10hl)
