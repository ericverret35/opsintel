---
layout: post
title: You're rethrowing errors and losing context. `Error.cause` fixes that.
date: '2026-07-21'
category: tech-news
source: Dev.to
url: https://dev.to/parsajiravand/youre-rethrowing-errors-and-losing-context-errorcause-fixes-that-4l97
tags:
- tech-news
- dev.to
---

## You're rethrowing errors and losing context. `Error.cause` fixes that.

**Source**: Dev.to

 Error handling has a quiet problem. You catch an error deep in a call stack, wrap it in something more descriptive, and rethrow. The caller gets a meaningful message — but the original error, with its stack trace and details, is gone. 
 

 
   async   function   loadUser  (  id  )   { 
   try   { 
     const   res   =   await   fetch  (  `/api/users/  ${  id  }  `  ); 
     if   (  !  res  .  ok  )   throw   new   Error  (  `HTTP   ${  res  .  status  }  `  ); 
     return   await   res  .  jso

**Lien**: [Lire](https://dev.to/parsajiravand/youre-rethrowing-errors-and-losing-context-errorcause-fixes-that-4l97)
