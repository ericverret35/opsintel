---
layout: post
title: Replace Semgrep, Trivy, and Gitleaks scripts with one scan gate
date: '2026-10-19'
category: tech-news
source: Dev.to
url: https://dev.to/wenping/replace-semgrep-trivy-and-gitleaks-scripts-with-one-scan-gate-4pnb
tags:
- tech-news
- dev.to
---

## Replace Semgrep, Trivy, and Gitleaks scripts with one scan gate

**Source**: Dev.to

 The merge request is green, then release is blocked by a secret or dependency CVE—usually because Semgrep, Trivy, and Gitleaks each own a job: three logs, three exit codes, no shared Finding, no shared suppressions. 

 
  Takeaway:  Put SAST (static application security testing), secret scanning, and SCA (software composition analysis for deps/artifacts/images) into  one scan job , normalize to one Finding model, then apply policy for  PASSED  /  FAILED  /  SKIPPED . Community edition is GPL-3.

**Lien**: [Lire](https://dev.to/wenping/replace-semgrep-trivy-and-gitleaks-scripts-with-one-scan-gate-4pnb)
