---
layout: post
title: 'PyGo: A Deep Learning Framework Where Go Calls Python Calls C++'
date: '2026-07-19'
category: tech-news
source: Dev.to
url: https://dev.to/sarkaragi/pygo-a-deep-learning-framework-where-go-calls-python-calls-c-4amo
tags:
- tech-news
- dev.to
---

## PyGo: A Deep Learning Framework Where Go Calls Python Calls C++

**Source**: Dev.to

  [Project] PyGo – embedding CPython inside a Go process to build a deep learning framework  

 I've been working on something a bit unusual: a deep learning framework where Go is the top-level API, Python handles autograd and the model zoo, and C++/CUDA does the raw compute. 

 The architecture looks like this: 
 

 
  Go API → CGo bridge → CPython (embedded) → pybind11 → CUDA/AVX-512 kernels
  

 



 The key insight: instead of a Python sidecar in every pod, CPython runs  inside  the Go binar

**Lien**: [Lire](https://dev.to/sarkaragi/pygo-a-deep-learning-framework-where-go-calls-python-calls-c-4amo)
