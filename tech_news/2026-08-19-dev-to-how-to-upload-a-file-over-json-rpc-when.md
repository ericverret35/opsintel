---
layout: post
title: How to upload a file over JSON-RPC, when JSON has no type for a file
date: '2026-08-19'
category: tech-news
source: Dev.to
url: https://dev.to/otezvikentiy/how-to-upload-a-file-over-json-rpc-when-json-has-no-type-for-a-file-5g76
tags:
- tech-news
- dev.to
---

## How to upload a file over JSON-RPC, when JSON has no type for a file

**Source**: Dev.to

 JSON has no representation for a file. Strings, numbers, arrays, objects - that is the whole list. So every JSON-RPC API eventually runs into the same question: how do you accept a file upload - a photo, a scan, a PDF - when the protocol itself cannot carry binary data? 

 The usual answer is: you don't. The file goes to a separate, ordinary controller that reads  $request-&gt;files , and the JSON-RPC layer handles everything else next to it. And now you have exactly the ad hoc endpoint sprawl 

**Lien**: [Lire](https://dev.to/otezvikentiy/how-to-upload-a-file-over-json-rpc-when-json-has-no-type-for-a-file-5g76)
