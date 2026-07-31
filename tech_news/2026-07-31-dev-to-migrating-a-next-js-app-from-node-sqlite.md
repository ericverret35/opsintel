---
layout: post
title: Migrating a Next.js app from node:sqlite to Cloudflare D1
date: '2026-07-31'
category: tech-news
source: Dev.to
url: https://dev.to/hirodeath/migrating-a-nextjs-app-from-nodesqlite-to-cloudflare-d1-225i
tags:
- tech-news
- dev.to
---

## Migrating a Next.js app from node:sqlite to Cloudflare D1

**Source**: Dev.to

 
 This is an English translation of my original Japanese article on  Zenn . 
 

 I had a small Next.js app that ran locally with Node.js and a SQLite file. When I decided to deploy it to Cloudflare Workers so I could use it away from my desk, the database layer had to change. The app used Node's built-in  node:sqlite  module, which is not available in the Workers runtime. 

 I moved the database to Cloudflare D1. The SQL used by this app did not need to change. Most of the work was converting t

**Lien**: [Lire](https://dev.to/hirodeath/migrating-a-nextjs-app-from-nodesqlite-to-cloudflare-d1-225i)
