---
layout: post
title: 'Luhn and IBAN check digits explained: validating card numbers and bank accounts
  in Python'
date: '2026-11-19'
category: tech-news
source: Dev.to
url: https://dev.to/quantumbreakz/luhn-and-iban-check-digits-explained-validating-card-numbers-and-bank-accounts-in-python-1oli
tags:
- tech-news
- dev.to
---

## Luhn and IBAN check digits explained: validating card numbers and bank accounts in Python

**Source**: Dev.to

 A  check digit  is an extra digit computed from the others, so a typo makes the number invalid. Card numbers use the  Luhn algorithm : double every second digit from the right, subtract 9 from any result above 9, add everything up, and the total must end in 0.  IBANs  use  mod 97 : move the first four characters to the end, turn letters into numbers (A = 10 … Z = 35), and the result divided by 97 must leave a remainder of 1. Both catch typos before you call a payment API. Neither tells you the 

**Lien**: [Lire](https://dev.to/quantumbreakz/luhn-and-iban-check-digits-explained-validating-card-numbers-and-bank-accounts-in-python-1oli)
