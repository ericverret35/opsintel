---
layout: post
title: How do you simulate a file drag-and-drop operation with Playwright when there's
  no direct `<input type=\"file\">` elemen
date: '2026-11-09'
category: tech-news
source: Dev.to
url: https://dev.to/styrow_dev/how-do-you-simulate-a-file-drag-and-drop-operation-with-playwright-when-theres-no-direct-input-54de
tags:
- tech-news
- dev.to
---

## How do you simulate a file drag-and-drop operation with Playwright when there's no direct `<input type=\"file\">` elemen

**Source**: Dev.to

 🤯 Playwright Challenge: Simulating File Drag-and-Drop WITHOUT  &lt;input type="file"&gt; ! 
Ever faced a modern web app where file uploads rely purely on drag-and-drop zones, leaving  locator.setInputFiles()  useless? It's a common automation hurdle. 

  📌 Problem Statement  
Many modern web apps use drag-and-drop for file uploads, skipping  &lt;input type="file"&gt; . Playwright's  setInputFiles()  is useless here. Instead, these UIs depend on native  dragenter ,  dragover , and  drop  DOM eve

**Lien**: [Lire](https://dev.to/styrow_dev/how-do-you-simulate-a-file-drag-and-drop-operation-with-playwright-when-theres-no-direct-input-54de)
