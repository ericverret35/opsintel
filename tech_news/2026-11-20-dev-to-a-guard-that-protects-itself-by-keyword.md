---
layout: post
title: A guard that protects itself by keyword ends up blocking you from reading it
date: '2026-11-20'
category: tech-news
source: Dev.to
url: https://dev.to/igorganapolsky/a-guard-that-protects-itself-by-keyword-ends-up-blocking-you-from-reading-it-4lb3
tags:
- tech-news
- dev.to
---

## A guard that protects itself by keyword ends up blocking you from reading it

**Source**: Dev.to

 Yesterday we added a credential guard to Mac YOLO Safeguards. It is a hook that runs before every shell command or file read an AI coding agent makes on your Mac, and it denies the ones that touch the keychain, copy a browser's credential store, or strip the quarantine flag from a download. A guard like that has to protect itself too, because the cheapest way for an agent to get around it is to edit its config or delete it. So the first version had a rule: deny any command that changes the guar

**Lien**: [Lire](https://dev.to/igorganapolsky/a-guard-that-protects-itself-by-keyword-ends-up-blocking-you-from-reading-it-4lb3)
