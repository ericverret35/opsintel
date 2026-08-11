---
layout: post
title: Keep logged in to Claude between container builds
date: '2026-08-11'
category: tech-news
source: Dev.to
url: https://dev.to/sukkergris/keep-logged-in-to-claude-between-container-builds-430h
tags:
- tech-news
- dev.to
---

## Keep logged in to Claude between container builds

**Source**: Dev.to

 This post is targeted devcontainer users not running the containers as root! 
 

 
         "remoteUser"  :     "root"  ,     #     Not     for     you!  
   

 



 In the end, this is basically a post about mounting folders and ensuring the right folder permissions - when not running with root permissions or as the root user. 

 You probably have a setup looking something like this: 
 devcontainer.json  
 

 
   {  
      "name"  :     "Customer-Name - Dev machine - Debian"  ,  
      "docker

**Lien**: [Lire](https://dev.to/sukkergris/keep-logged-in-to-claude-between-container-builds-430h)
