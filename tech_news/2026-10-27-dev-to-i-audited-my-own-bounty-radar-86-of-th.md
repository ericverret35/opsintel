---
layout: post
title: 'I audited my own bounty radar: 86% of the "Algora bounties" I was tracking
  weren''t real'
date: '2026-10-27'
category: tech-news
source: Dev.to
url: https://dev.to/rovidev/i-audited-my-own-bounty-radar-86-of-the-algora-bounties-i-was-tracking-werent-real-2plj
tags:
- tech-news
- dev.to
---

## I audited my own bounty radar: 86% of the "Algora bounties" I was tracking weren't real

**Source**: Dev.to

 I run a small radar that lists paid GitHub issues (Algora, Opire, IssueHunt, BountyHub, TaskBounty). Recently I audited my own feed and found it was wrong in an instructive way. Here is what I got wrong, and the check that fixes it. 

 
  
  
  The mistake: trusting text on the issue
 

 My scanner treated  "/bounty $700" in:body  as proof of an Algora bounty. That query matches roughly  67,000  open issues on GitHub. Of the 97 issues I had flagged as verified Algora bounties,  83 (86%)  had no

**Lien**: [Lire](https://dev.to/rovidev/i-audited-my-own-bounty-radar-86-of-the-algora-bounties-i-was-tracking-werent-real-2plj)
