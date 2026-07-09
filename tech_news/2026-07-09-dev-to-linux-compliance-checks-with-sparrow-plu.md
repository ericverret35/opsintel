---
layout: post
title: Linux compliance checks with Sparrow plugin
date: '2026-07-09'
category: tech-news
source: Dev.to
url: https://dev.to/melezhik/linux-compliance-checks-with-sparrow-plugin-2160
tags:
- tech-news
- dev.to
---

## Linux compliance checks with Sparrow plugin

**Source**: Dev.to

 Sparrow is Raku automation framework comes with useful plugins people can use to automate infrastructure. Scc plugin allows to check Linux essential configuration files for security compliance. Here some examples: 

 Sysctl 
 

 
   $     sudo  sysctl  -a   | s6  --plg-run  scc@check = sysctl
 12:24:07 :: [task] - run plg scc@check=sysctl
12:24:07 :: [task] - run [scc], thing: scc@check=sysctl
[task run: task.bash - scc]
[task stdout]
12:24:08 :: abi.cp15_barrier = 1
12:24:08 :: abi.setend = 1


**Lien**: [Lire](https://dev.to/melezhik/linux-compliance-checks-with-sparrow-plugin-2160)
