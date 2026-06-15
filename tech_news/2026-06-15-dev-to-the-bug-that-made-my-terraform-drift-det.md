---
layout: post
title: The bug that made my Terraform drift detector cry wolf (and the one-line fix)
date: '2026-06-15'
category: tech-news
source: Dev.to
url: https://dev.to/hitoshi1964/the-bug-that-made-my-terraform-drift-detector-cry-wolf-and-the-one-line-fix-49ai
tags:
- tech-news
- dev.to
---

## The bug that made my Terraform drift detector cry wolf (and the one-line fix)

**Source**: Dev.to

  terraform plan  tells you what  Terraform  changed. It says nothing about the 
RDS parameter someone tweaked in the console at 2am, or the security group rule 
added by hand during an incident. To catch  that  kind of drift, you have to 
compare your tfstate against what AWS actually returns from the API — yourself. 

 I built exactly that, and the first version was useless. Not because the diff 
was wrong, but because it screamed about drift on every single resource, every 
single time. Here'

**Lien**: [Lire](https://dev.to/hitoshi1964/the-bug-that-made-my-terraform-drift-detector-cry-wolf-and-the-one-line-fix-49ai)
