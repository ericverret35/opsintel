---
layout: post
title: I reverted the fix in 181 real changes to see if the tests would notice
date: '2026-09-30'
category: tech-news
source: Dev.to
url: https://dev.to/syntaxixr/i-reverted-the-fix-in-181-real-changes-to-see-if-the-tests-would-notice-2e3
tags:
- tech-news
- dev.to
---

## I reverted the fix in 181 real changes to see if the tests would notice

**Source**: Dev.to

 I keep running into the same thing with coding agents. The agent fixes a bug, adds a test, CI goes green, and it says "done". But green only means the test passes. It doesn't mean the test would have failed before the fix. And if it wouldn't, it checks nothing about the bug, however green it is. 

 The old-school way to find out is boring: revert the fix and run the test again. So I wrote a tool that does exactly that for every test in a change, and pointed it at the real history of 17 open-sou

**Lien**: [Lire](https://dev.to/syntaxixr/i-reverted-the-fix-in-181-real-changes-to-see-if-the-tests-would-notice-2e3)
