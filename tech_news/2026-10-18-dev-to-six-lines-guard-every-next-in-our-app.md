---
layout: post
title: Six lines guard every ?next= in our app, and the case people miss is a backslash
date: '2026-10-18'
category: tech-news
source: Dev.to
url: https://dev.to/daniel_pertu/six-lines-guard-every-next-in-our-app-and-the-case-people-miss-is-a-backslash-5234
tags:
- tech-news
- dev.to
---

## Six lines guard every ?next= in our app, and the case people miss is a backslash

**Source**: Dev.to

 Two places in Munchable read a destination out of a query string. The OAuth callback: 
 

 
   // GET /auth/callback?code=...&amp;next=/... 
 const   next   =   safeReturnPath  (  searchParams  .  get  (  '  next  '  ),   '  /  '  ); 
 if   (  code  )   { 
   const   {   error   }   =   await   supabase  .  auth  .  exchangeCodeForSession  (  code  ); 
   if   (  !  error  )   return   NextResponse  .  redirect  (  new   URL  (  next  ,   origin  )); 
 } 
  

 



 And the sign-in page, where a

**Lien**: [Lire](https://dev.to/daniel_pertu/six-lines-guard-every-next-in-our-app-and-the-case-people-miss-is-a-backslash-5234)
