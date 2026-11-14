---
layout: post
title: 'How to politely quit every open app on macOS, Linux and Windows (and the bug
  my tests missed) published: false'
date: '2026-11-14'
category: tech-news
source: Dev.to
url: https://dev.to/abhisheksinhaleakyally/how-to-politely-quit-every-open-app-on-macos-linux-and-windows-and-the-bug-my-tests-missed-2760
tags:
- tech-news
- dev.to
---

## How to politely quit every open app on macOS, Linux and Windows (and the bug my tests missed) published: false

**Source**: Dev.to

 At the end of most days I have 15+ apps open. I wanted one command that closes them all, except the terminal I'm typing in,  without  losing unsaved work. 

  killall  and  taskkill /f  are out: they kill processes, and unsaved documents die with them. What I wanted was the same thing as pressing Cmd+Q or clicking the X on every app: a polite request the app can answer with "Save changes?". 

 So I built  lightsout , a small Go CLI. This post covers how "quit politely" works on each OS, and the

**Lien**: [Lire](https://dev.to/abhisheksinhaleakyally/how-to-politely-quit-every-open-app-on-macos-linux-and-windows-and-the-bug-my-tests-missed-2760)
