---
layout: post
title: Docker
date: '2026-09-16'
category: tech-news
source: Dev.to
url: https://dev.to/nithu_varshini_/docker-268h
tags:
- tech-news
- dev.to
---

## Docker

**Source**: Dev.to

 
  
  
   Docker Desktop 
 

 1.Open terminal 
    

 2.Run 
 

 
  docker pull nginx
docker pull httpd
docker pull docker/getting-started
  

 



 in docker hub terminal to pull docker images 

 3.To create a container run 
 

 
  docker run  -idt  nginx
  

 



 it will give the container ID 

 4.Port Mapping  (  -p &lt;HOST-PORT&gt;:&lt;CONTAINER_PORT&gt;  ) for creating container after creating image 
run  docker run -idt -p 80:80 nginx  
    

  docker run -idt -p 81:80 httpd  
    

  d

**Lien**: [Lire](https://dev.to/nithu_varshini_/docker-268h)
