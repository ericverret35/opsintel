---
layout: post
title: Code Review From the Terminal and CI, No MCP Client Required
date: '2026-08-16'
category: tech-news
source: Dev.to
url: https://dev.to/goodjobwilliam/code-review-from-the-terminal-and-ci-no-mcp-client-required-33jf
tags:
- tech-news
- dev.to
---

## Code Review From the Terminal and CI, No MCP Client Required

**Source**: Dev.to

 A month ago I shipped  aicraft-code-review , an MCP server that reviews code locally. This week I added a CLI mode — because not everyone wants to wire up an MCP client just to check a diff. 

 Now the same reviewer runs three ways: 

 
 
 MCP tools  —  review_code  /  review_diff  /  review_file  inside Claude Code, Cursor, Cline 
 
 CLI  —  mcp-code-review review-file path/to/file.py 
 
 
 CI  — pipe  git diff  into it and branch on the exit code 
 

 
  
  
  The CLI
 



 
  pip  install  a

**Lien**: [Lire](https://dev.to/goodjobwilliam/code-review-from-the-terminal-and-ci-no-mcp-client-required-33jf)
