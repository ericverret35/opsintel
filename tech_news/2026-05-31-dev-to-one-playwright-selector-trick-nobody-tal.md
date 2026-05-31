---
layout: post
title: 'One Playwright Selector Trick Nobody Talks About: getByRole'
date: '2026-05-31'
category: tech-news
source: Dev.to
url: https://dev.to/sian-agency/one-playwright-selector-trick-nobody-talks-about-getbyrole-100e
tags:
- tech-news
- dev.to
---

## One Playwright Selector Trick Nobody Talks About: getByRole

**Source**: Dev.to

 Everyone reaches for  page.locator(".some-class")  first. They shouldn't. 

  getByRole  is the most stable selector in Playwright and almost nobody uses it for scraping. They think it's a testing-library thing. It's not. It's a way of asking the page "what is this element semantically" instead of "what classname does the design system happen to use this week." 

 That distinction is what kept our Facebook video transcript actor running through three Facebook redesigns this past year. 

 
  
  

**Lien**: [Lire](https://dev.to/sian-agency/one-playwright-selector-trick-nobody-talks-about-getbyrole-100e)
