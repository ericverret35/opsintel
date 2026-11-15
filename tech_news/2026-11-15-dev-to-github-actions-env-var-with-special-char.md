---
layout: post
title: GitHub Actions env var with special characters in a run step
date: '2026-11-15'
category: tech-news
source: Dev.to
url: https://dev.to/kalemi/github-actions-env-var-with-special-characters-in-a-run-step-2k9n
tags:
- tech-news
- dev.to
---

## GitHub Actions env var with special characters in a run step

**Source**: Dev.to

 A GitHub Actions env var with special characters breaks a run step because of an ordering detail that is easy to have backwards: an expression is substituted into the script as text before any shell is started, so the shell parses your value as if you had typed it. Quoting the reference in the script does not help, because by then the value is the script. 

     
 Substitution happens while the script file is written. The shell is started afterwards and sees only the finished text.  
 
  
  
  

**Lien**: [Lire](https://dev.to/kalemi/github-actions-env-var-with-special-characters-in-a-run-step-2k9n)
