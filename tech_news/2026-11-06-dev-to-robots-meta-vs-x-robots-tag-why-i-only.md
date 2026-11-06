---
layout: post
title: 'Robots meta vs X-Robots-Tag: why I only use the meta tag'
date: '2026-11-06'
category: tech-news
source: Dev.to
url: https://dev.to/mobeenahmedgondal/robots-meta-vs-x-robots-tag-why-i-only-use-the-meta-tag-15li
tags:
- tech-news
- dev.to
---

## Robots meta vs X-Robots-Tag: why I only use the meta tag

**Source**: Dev.to

 I run a small tool site on plain PHP shared hosting, and one of the smallest decisions I made still shapes how I handle every new page: I control crawlers with a  &lt;meta name="robots"&gt;  tag in the HTML, and I never touch the  X-Robots-Tag  HTTP header. 

 Both do the same job. A robots meta tag lives inside the page and tells a search engine whether to index that page, follow its links, or show a snippet. The X-Robots-Tag does exactly the same thing, but it is sent as an HTTP response head

**Lien**: [Lire](https://dev.to/mobeenahmedgondal/robots-meta-vs-x-robots-tag-why-i-only-use-the-meta-tag-15li)
