---
layout: post
title: Integrating Sentry into Tauri 2 without losing the local crash log
date: '2026-11-19'
category: tech-news
source: Dev.to
url: https://dev.to/onone1916/integrating-sentry-into-tauri-2-without-losing-the-local-crash-log-203l
tags:
- tech-news
- dev.to
---

## Integrating Sentry into Tauri 2 without losing the local crash log

**Source**: Dev.to

 LumenPod is a Tauri 2 media library. If the Rust process panicked, the explanation went to stderr. Someone could send me the app's diagnostic bundle and I'd see a Rust log that stopped just before the line I needed. 

 When I added Sentry, I still wanted that line locally, even if the user had turned off crash reporting. I also had to decide how much of a panic belonged in a bundle someone might share. An error during an import can include the full path to their video. 

 
  
  
  Give the clie

**Lien**: [Lire](https://dev.to/onone1916/integrating-sentry-into-tauri-2-without-losing-the-local-crash-log-203l)
