---
layout: post
title: 'Validating a Pakistani CNIC number: the 13-digit format, what the digits mean,
  and what format checks can''t tell you'
date: '2026-11-19'
category: tech-news
source: Dev.to
url: https://dev.to/quantumbreakz/validating-a-pakistani-cnic-number-the-13-digit-format-what-the-digits-mean-and-what-format-3b2
tags:
- tech-news
- dev.to
---

## Validating a Pakistani CNIC number: the 13-digit format, what the digits mean, and what format checks can't tell you

**Source**: Dev.to

 A Pakistani  CNIC number  has  13 digits , written  12345-1234567-1 : a five-digit  locality code , a seven-digit  serial , and a final digit. By widely documented convention the  first digit is the region  (3 is Punjab, 4 is Sindh, and so on) and the  last digit encodes gender , odd for male and even for female. What it  doesn't  have is a check digit: unlike a  passport's MRZ , a mistyped CNIC number can't be detected from the number alone. So format validation catches badly formed input, and

**Lien**: [Lire](https://dev.to/quantumbreakz/validating-a-pakistani-cnic-number-the-13-digit-format-what-the-digits-mean-and-what-format-3b2)
