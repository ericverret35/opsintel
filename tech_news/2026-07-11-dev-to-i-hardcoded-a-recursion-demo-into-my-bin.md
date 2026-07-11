---
layout: post
title: I Hardcoded a Recursion Demo Into My Binary Converter and I Regret Nothing
date: '2026-07-11'
category: tech-news
source: Dev.to
url: https://dev.to/patrick_mbithi_/i-hardcoded-a-recursion-demo-into-my-binary-converter-and-i-regret-nothing-2k9n
tags:
- tech-news
- dev.to
---

## I Hardcoded a Recursion Demo Into My Binary Converter and I Regret Nothing

**Source**: Dev.to

 I built a decimal-to-binary converter and then, for no good reason, decided that if you typed in the number 5, it should not just show you the answer. It should show you the call stack. 

 Here's the actual conversion logic. Nothing fancy: 
 

 
   const   decimalToBinary   =   (  input  )   =&gt;   { 
   if   (  input   ===   0   ||   input   ===   1  )   { 
     return   String  (  input  ); 
   }   else   { 
     return   decimalToBinary  (  Math  .  floor  (  input   /   2  ))   +   (  inpu

**Lien**: [Lire](https://dev.to/patrick_mbithi_/i-hardcoded-a-recursion-demo-into-my-binary-converter-and-i-regret-nothing-2k9n)
