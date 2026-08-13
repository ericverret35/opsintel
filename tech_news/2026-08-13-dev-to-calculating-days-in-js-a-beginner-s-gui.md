---
layout: post
title: 'Calculating Days in JS: A Beginner''s Guide'
date: '2026-08-13'
category: tech-news
source: Dev.to
url: https://dev.to/kahenda/calculating-days-in-js-a-beginners-guide-1ii8
tags:
- tech-news
- dev.to
---

## Calculating Days in JS: A Beginner's Guide

**Source**: Dev.to

 Ever wanted to know what numerical "day of the year" a date falls on (e.g., January 31st is day 31, but February 1st is day 32)? 

 We can do this easily by subtracting January 1st from our target date and converting milliseconds into days! 

 JavaScript 
function dayOfTheYear(date) { 
  const year = date.getFullYear(); 

 // Get January 1st of that exact year 
  const startOfYear = new Date(year, 0, 1); 

 // Find the difference in milliseconds 
  const diffTime = date.getTime() - startOfYear.

**Lien**: [Lire](https://dev.to/kahenda/calculating-days-in-js-a-beginners-guide-1ii8)
