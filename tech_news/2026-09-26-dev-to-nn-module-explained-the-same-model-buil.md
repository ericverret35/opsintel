---
layout: post
title: 'nn.Module Explained: The Same Model Built with Raw Tensors and with nn.Module'
date: '2026-09-26'
category: tech-news
source: Dev.to
url: https://dev.to/pytorchfromgroundup/nnmodule-explained-the-same-model-built-with-raw-tensors-and-with-nnmodule-1ccl
tags:
- tech-news
- dev.to
---

## nn.Module Explained: The Same Model Built with Raw Tensors and with nn.Module

**Source**: Dev.to

 Every PyTorch model is a subclass of  nn.Module . This article explains what that class does by building the same model two ways: first with raw tensors only, then with  nn.Module . Comparing the two shows exactly which parts of the work the module takes over. 

 
  
  
  The problem
 

 The model learns the line  y = 3x + 1  from 20 noisy points. 
 

 
   import   torch 

 torch  .  manual_seed  (  0  ) 
 x   =   torch  .  linspace  (  0  ,   2  ,   20  ).  unsqueeze  (  1  )        # shape (2

**Lien**: [Lire](https://dev.to/pytorchfromgroundup/nnmodule-explained-the-same-model-built-with-raw-tensors-and-with-nnmodule-1ccl)
