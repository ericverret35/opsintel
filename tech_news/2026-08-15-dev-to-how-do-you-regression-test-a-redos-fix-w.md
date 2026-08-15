---
layout: post
title: How do you regression-test a ReDoS fix without hanging CI?
date: '2026-08-15'
category: tech-news
source: Dev.to
url: https://dev.to/tanya_monoware/how-do-you-regression-test-a-redos-fix-without-hanging-ci-1al3
tags:
- tech-news
- dev.to
---

## How do you regression-test a ReDoS fix without hanging CI?

**Source**: Dev.to

 A known-bad regex is useful evidence, but putting it directly in the test process can hang the runner before the timeout assertion fires. 

 The boundary I am using: 

 
 run each adversarial case in a fresh worker thread or child process 
 let the parent own a hard timeout and terminate the child 
 keep semantic-parity fixtures separate from timing guards 
 require the safer replacement to pass both suites 
 record the timeout class and bounded elapsed time as evidence 
 

 Browser workers hav

**Lien**: [Lire](https://dev.to/tanya_monoware/how-do-you-regression-test-a-redos-fix-without-hanging-ci-1al3)
