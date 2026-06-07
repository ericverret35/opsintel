---
layout: post
title: 9 silent-row-loss fixes in 7 days across 7 OSS databases
date: '2026-06-07'
category: tech-news
source: Dev.to
url: https://dev.to/sravan27/9-silent-row-loss-fixes-in-7-days-across-7-oss-databases-2nd-draft-56da
tags:
- tech-news
- dev.to
---

## 9 silent-row-loss fixes in 7 days across 7 OSS databases

**Source**: Dev.to

 A pattern: a JavaScript database re-implements four common SQL operators -  upper / lower ,  length / substr , case-insensitive match, range comparison. The implementation looks right. The tests pass. The CI is green. And then the moment a user's data contains the German  ß , a fi ligature, an emoji, a Turkish dotted-i, or a CJK Extension B character, the operator silently returns the wrong rows. No error. No log. Just less data than the user expected, or the wrong data. 

 I've now shipped thi

**Lien**: [Lire](https://dev.to/sravan27/9-silent-row-loss-fixes-in-7-days-across-7-oss-databases-2nd-draft-56da)
