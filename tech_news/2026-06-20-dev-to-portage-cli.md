---
layout: post
title: portage-cli
date: '2026-06-20'
category: tech-news
source: Dev.to
url: https://dev.to/luzero/portage-cli-4b3f
tags:
- tech-news
- dev.to
---

## portage-cli

**Source**: Dev.to

 I'm experimenting with an alternative implementation of  portage  in Rust. 

 It is quite different from  pkgcraft  even if both projects have similar targets. 

 Main differences: 

 
 separation of concerns:  portage-cli  is based on a set of layered crates, that let people reuse specific parts of it.  pkgcraft  on the other hand is a bit monolithic right now. 
 pure-rust:  pkgcraft  for correctness  wraps bash ,  portage-repo  leverages  brush  fixing issues as  they are found . 
 focus on d

**Lien**: [Lire](https://dev.to/luzero/portage-cli-4b3f)
