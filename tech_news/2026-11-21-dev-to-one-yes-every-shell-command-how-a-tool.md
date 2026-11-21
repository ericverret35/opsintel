---
layout: post
title: 'One Yes, Every Shell Command: How a Tool-Name Approval Cache (CVE-2026-56074)
  Turns a Click Into a Standing Grant'
date: '2026-11-21'
category: tech-news
source: Dev.to
url: https://dev.to/ginigenai_hp_0ae441ead91f/one-yes-every-shell-command-how-a-tool-name-approval-cache-cve-2026-56074-turns-a-click-into-a-5dgc
tags:
- tech-news
- dev.to
---

## One Yes, Every Shell Command: How a Tool-Name Approval Cache (CVE-2026-56074) Turns a Click Into a Standing Grant

**Source**: Dev.to

 
  
  
  TL;DR
 

 
 CVE-2026-56074 (GitHub advisory GHSA-ffp3-3562-8cv3, CVSS 3.1 score 5.5, CWE-863) describes an agent framework whose approval system cached consent by  tool name only . Approve  execute_command  once for  ls -la , and later calls to the same tool skipped the prompt for the rest of the execution context. 
 The prompt text named the specific command, so the human believed they were approving one call. The system enforced something much broader: "this tool is trusted now." 
 I

**Lien**: [Lire](https://dev.to/ginigenai_hp_0ae441ead91f/one-yes-every-shell-command-how-a-tool-name-approval-cache-cve-2026-56074-turns-a-click-into-a-5dgc)
