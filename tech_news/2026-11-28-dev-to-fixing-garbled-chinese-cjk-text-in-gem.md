---
layout: post
title: Fixing Garbled Chinese (CJK) Text in Gemini CLI on Windows
date: '2026-11-28'
category: tech-news
source: Dev.to
url: https://dev.to/_gary_f8a5c9d66a48f501/fixing-garbled-chinese-cjk-text-in-gemini-cli-on-windows-21i2
tags:
- tech-news
- dev.to
---

## Fixing Garbled Chinese (CJK) Text in Gemini CLI on Windows

**Source**: Dev.to

 If you run Gemini CLI on Windows and the terminal spits out  garbled Chinese (or any CJK), question marks, or little boxes , it's almost never a bug in Gemini CLI itself. The real cause is an  encoding mismatch : the Windows CMD / PowerShell default is often Big5 (code page cp950) for a Traditional-Chinese system, while Gemini CLI (a Node app) outputs UTF-8. When the two don't match, you get mojibake. 

 This post walks the fix in order —  terminal → font → system → file encoding . Try the firs

**Lien**: [Lire](https://dev.to/_gary_f8a5c9d66a48f501/fixing-garbled-chinese-cjk-text-in-gemini-cli-on-windows-21i2)
