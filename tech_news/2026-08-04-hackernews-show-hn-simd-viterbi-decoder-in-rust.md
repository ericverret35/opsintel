---
layout: post
title: 'Show HN: SIMD Viterbi Decoder in Rust'
date: '2026-08-04'
category: tech-news
source: HackerNews
url: https://github.com/brian-armstrong/fec
tags:
- tech-news
- hackernews
---

## Show HN: SIMD Viterbi Decoder in Rust

**Source**: HackerNews

 I wrote libcorrect in C in 2016 and wanted to revisit it in Rust. Instead of doing just a direct conversion, I went down the rabbit hole of making Rust's std::simd work for me. I ended up with a templated, generic Viterbi decoder for convolutional codes that dispatches the decode at runtime depending on which instruction sets are available. For small rates and orders, the entire decode lives in registers. Larger codes work through memory but take advantage of some acceleration structures. I als

**Lien**: [Lire](https://github.com/brian-armstrong/fec)
