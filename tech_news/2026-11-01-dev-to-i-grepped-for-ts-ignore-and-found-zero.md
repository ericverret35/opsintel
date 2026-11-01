---
layout: post
title: I grepped for @ts-ignore and found zero. Then I grepped for the cast nobody
  bans
date: '2026-11-01'
category: tech-news
source: Dev.to
url: https://dev.to/chet103cc/i-grepped-for-ts-ignore-and-found-zero-then-i-grepped-for-the-cast-nobody-bans-723
tags:
- tech-news
- dev.to
---

## I grepped for @ts-ignore and found zero. Then I grepped for the cast nobody bans

**Source**: Dev.to

 Every TypeScript team has a rule about  @ts-ignore . Ours does too, and it works:  zero occurrences across 610 source files . 

 Then I grepped for something nobody puts in a style guide: 
 

 
   grep   -rn   --include  =  '*.ts'   --include  =  '*.tsx'   \ 
   --exclude-dir  = node_modules  --exclude-dir  = .next  \ 
   'as unknown as'  apps packages |  wc   -l 
  

 



  117.  

 Zero explicit suppressions, a hundred and seventeen implicit ones. That ratio is not a coincidence — it is what 

**Lien**: [Lire](https://dev.to/chet103cc/i-grepped-for-ts-ignore-and-found-zero-then-i-grepped-for-the-cast-nobody-bans-723)
