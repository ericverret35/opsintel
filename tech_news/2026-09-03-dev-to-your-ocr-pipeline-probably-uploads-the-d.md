---
layout: post
title: Your OCR pipeline probably uploads the document. It doesn't have to
date: '2026-09-03'
category: tech-news
source: Dev.to
url: https://dev.to/mykola_melnyk_ml/your-ocr-pipeline-probably-uploads-the-document-it-doesnt-have-to-5c9d
tags:
- tech-news
- dev.to
---

## Your OCR pipeline probably uploads the document. It doesn't have to

**Source**: Dev.to

     

  Written 2026-09-03. Code examples target  @stabrise/scaledp@0.1.1 . No prior OCR or ONNX knowledge assumed.  

  TL;DR:  Every mainstream OCR API has the same architecture — your document goes over the wire to someone else's disk. Browser-native inference removes that box entirely:   @stabrise/scaledp   runs PDF rendering, text detection, OCR and entity recognition on  onnxruntime-web , in the tab, with no upload. That is a real win for sensitive documents and a real cost in first-load 

**Lien**: [Lire](https://dev.to/mykola_melnyk_ml/your-ocr-pipeline-probably-uploads-the-document-it-doesnt-have-to-5c9d)
