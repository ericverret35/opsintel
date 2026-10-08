---
layout: post
title: How to show a line above the prompt in Claude Code with a mod (band, status
  line, toast)
date: '2026-10-08'
category: tech-news
source: Dev.to
url: https://dev.to/nakadadev/how-to-show-a-line-above-the-prompt-in-claude-code-with-a-mod-band-status-line-toast-3947
tags:
- tech-news
- dev.to
---

## How to show a line above the prompt in Claude Code with a mod (band, status line, toast)

**Source**: Dev.to

 To always show a line right above the prompt, handle  ui.render  with  { component: 'AbovePrompt' }  and return a tree (the band). For a single line of text below the prompt, use  $.ui.status(text) . For a notification that disappears after a few seconds, use  $.ui.toast(text) . The last two need no render hook and can be called from anywhere in one line. 

 
  
  
  How they differ
 

  
 
 
 Thing 
 How to show it 
 How long it stays 
 Good for 
 
 
 
 
 Band 
 Return a tree from  ui.render  

**Lien**: [Lire](https://dev.to/nakadadev/how-to-show-a-line-above-the-prompt-in-claude-code-with-a-mod-band-status-line-toast-3947)
