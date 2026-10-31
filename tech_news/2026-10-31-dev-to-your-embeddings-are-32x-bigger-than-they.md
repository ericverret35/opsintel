---
layout: post
title: Your embeddings are 32x bigger than they need to be. Maybe.
date: '2026-10-31'
category: tech-news
source: Dev.to
url: https://dev.to/ahmad_shawar_de8d35d546cf/your-embeddings-are-32x-bigger-than-they-need-to-be-maybe-309h
tags:
- tech-news
- dev.to
---

## Your embeddings are 32x bigger than they need to be. Maybe.

**Source**: Dev.to

 Every OpenAI embedding you store in Postgres is 6 KB. A hundred million documents is 600 GB of vectors before you build a single index, and an HNSW index wants to live in RAM. That is how a RAG prototype turns into a database bill nobody planned for. 

 The fix sounds simple: store fewer bits per number. pgvector already has  halfvec  (16 bits) and  binary_quantize  (1 bit). VectorChord ships RaBitQ. TurboQuant from Google Research is the new name everyone mentions. Each one promises a smaller 

**Lien**: [Lire](https://dev.to/ahmad_shawar_de8d35d546cf/your-embeddings-are-32x-bigger-than-they-need-to-be-maybe-309h)
