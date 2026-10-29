---
layout: post
title: How to handle multiple VS Code windows at a time
date: '2026-10-29'
category: tech-news
source: Dev.to
url: https://dev.to/zhekpisov/how-to-handle-multiple-vs-code-windows-at-a-time-3phc
tags:
- tech-news
- dev.to
---

## How to handle multiple VS Code windows at a time

**Source**: Dev.to

 
  
  
  Native tabs
 

 
 Add "window.nativeTabs": true to your VS Code settings and restart VS Code. 
 After that you can merge all the windows into one window with tabs, one tab per repo (Window → Merge All Windows). 
 

 
  
  
  Add your own shortcuts
 

 VS Code has commands for moving between window tabs, but they come with no keys assigned. Open Command Palette → "Preferences: Open Keyboard Shortcuts (JSON)" and add: 
 

 
   [  
    {     "key"  :     "ctrl+cmd+right"  ,     "command" 

**Lien**: [Lire](https://dev.to/zhekpisov/how-to-handle-multiple-vs-code-windows-at-a-time-3phc)
