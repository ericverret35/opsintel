---
layout: post
title: Why your App Tracking Transparency prompt doesn't show up (and how it got my
  app rejected)
date: '2026-08-16'
category: tech-news
source: Dev.to
url: https://dev.to/ninomaedev/why-your-app-tracking-transparency-prompt-doesnt-show-up-and-how-it-got-my-app-rejected-oob
tags:
- tech-news
- dev.to
---

## Why your App Tracking Transparency prompt doesn't show up (and how it got my app rejected)

**Source**: Dev.to

 App Review rejected my iOS app under Guideline 2.1. The note said reviewers were unable to locate the App Tracking Transparency permission request when they tested the build. 

 The prompt worked on my iPhone. Every single launch. It just didn't work on theirs. 

 The cause turned out to be two properties of the ATT API that are easy to miss individually and genuinely nasty in combination: together they produce a bug that is invisible on a fast device and completely reproducible on a slow one. 

**Lien**: [Lire](https://dev.to/ninomaedev/why-your-app-tracking-transparency-prompt-doesnt-show-up-and-how-it-got-my-app-rejected-oob)
