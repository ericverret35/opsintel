---
layout: post
title: Quanta memoria serve a un LLM locale?
date: '2026-11-06'
category: tech-news
source: Dev.to
url: https://dev.to/bestaitools-it/quanta-memoria-serve-a-un-llm-locale-5cli
tags:
- tech-news
- dev.to
---

## Quanta memoria serve a un LLM locale?

**Source**: Dev.to

 Prima di scaricare un modello da eseguire in locale, la domanda è se ci sta in memoria. La stima è la somma di tre termini, confrontata con quello che la macchina può davvero dare al modello: 
 

 
  need = weights + KV cache + overhead
fits if need &lt;= 0.8 × usable memory
  

 



 I numeri qui sotto seguono la stima usata dal  browser dei modelli locali  nell'app desktop  osFoundry , verificata su quello che l'app mostra per un MacBook M3 da 16 GB. 

     

 
  
  
  I pesi
 

 I pesi sono 

**Lien**: [Lire](https://dev.to/bestaitools-it/quanta-memoria-serve-a-un-llm-locale-5cli)
