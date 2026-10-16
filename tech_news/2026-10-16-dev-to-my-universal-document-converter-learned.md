---
layout: post
title: My universal document converter learned that 'auto-detect' is a lie when the
  file extension lies
date: '2026-10-16'
category: tech-news
source: Dev.to
url: https://dev.to/imapphelp/my-universal-document-converter-learned-that-auto-detect-is-a-lie-when-the-file-extension-lies-493f
tags:
- tech-news
- dev.to
---

## My universal document converter learned that 'auto-detect' is a lie when the file extension lies

**Source**: Dev.to

 The idea behind the universal converter was simple: hand it any document, it figures out the type, converts to Markdown. No routing on the caller's side. One endpoint. 

 The failure mode I didn't plan for: a PDF that arrives named  report.docx . 

 A user sent a contract scanned to PDF, but their pipeline renamed it with a  .docx  extension because "that's what the upload widget defaults to." My sniffing logic checked the extension first, trusted it, fed the bytes to the DOCX parser, and got b

**Lien**: [Lire](https://dev.to/imapphelp/my-universal-document-converter-learned-that-auto-detect-is-a-lie-when-the-file-extension-lies-493f)
