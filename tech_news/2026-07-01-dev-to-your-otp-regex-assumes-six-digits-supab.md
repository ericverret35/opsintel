---
layout: post
title: Your OTP regex assumes six digits. Supabase magic links don't.
date: '2026-07-01'
category: tech-news
source: Dev.to
url: https://dev.to/incultnitollc/your-otp-regex-assumes-six-digits-supabase-magic-links-dont-33i1
tags:
- tech-news
- dev.to
---

## Your OTP regex assumes six digits. Supabase magic links don't.

**Source**: Dev.to

 Sign-in worked flawlessly in dev. Then a real user pasted a real code and got "invalid format" — before the code ever reached Supabase. The credential was fine. My regex was wrong. Here's the one-line assumption that broke auth for every human who wasn't me. 

 I run a Discord-native Company Brain. Teams  /save  docs and  /ask  grounded answers; access is gated by a magic-link claim that emails a one-time code. Standard GoTrue OTP flow. The client shows a box, you paste the code, the server ver

**Lien**: [Lire](https://dev.to/incultnitollc/your-otp-regex-assumes-six-digits-supabase-magic-links-dont-33i1)
