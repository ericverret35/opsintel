---
layout: post
title: Middleware is not your auth layer (a Next.js footgun I keep finding)
date: '2026-10-30'
category: tech-news
source: Dev.to
url: https://dev.to/somnath_khadanga_2e5c2364/middleware-is-not-your-auth-layer-a-nextjs-footgun-i-keep-finding-2n31
tags:
- tech-news
- dev.to
---

## Middleware is not your auth layer (a Next.js footgun I keep finding)

**Source**: Dev.to

 When I audit Next.js apps built quickly (often with AI tools), one pattern shows up more than any other: routes are protected in  middleware.ts , and the API route handlers trust that. 
 

 
   // app/api/admin/users/route.ts 
 export   async   function   GET  (  request  :   NextRequest  )   { 
   // "middleware already checked" 
   const   users   =   await   db  .  user  .  findMany  () 
   return   NextResponse  .  json  (  users  ) 
 } 
  

 



 Middleware can be skipped by a matcher that

**Lien**: [Lire](https://dev.to/somnath_khadanga_2e5c2364/middleware-is-not-your-auth-layer-a-nextjs-footgun-i-keep-finding-2n31)
