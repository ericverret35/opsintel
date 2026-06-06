---
layout: post
title: 把 Sa-Token 搬到 NestJS 生态：xlt-token 1.0 的几个设计取舍
date: '2026-06-06'
category: tech-news
source: Dev.to
url: https://dev.to/pengcheng_e679693a21e1180/ba-sa-token-ban-dao-nestjs-sheng-tai-xlt-token-10-de-ji-ge-she-ji-qu-she-4017
tags:
- tech-news
- dev.to
---

## 把 Sa-Token 搬到 NestJS 生态：xlt-token 1.0 的几个设计取舍

**Source**: Dev.to

 最近发布了  xlt-token@1.0.0-rc.1 ，一个为 NestJS 设计的 Token 鉴权库，灵感来自 Java 生态的  Sa-Token 。 

 仓库： github.com/xiaoLangtou/xlt-token  

 功能列表看起来不复杂——登录、登出、踢人、权限校验、会话存储——但动手实现时，每个"理应如此"的能力背后都有几个不那么显然的选择。这篇文章想聊聊其中几个，主要是为了自己复盘，也希望对做类似设计的人有参考价值。 




 
  
  
  为什么不直接用 Passport？
 

  @nestjs/passport  几乎是 NestJS 鉴权的默认答案，但它本质上是个 strategy 调度器——你提供策略（ local  /  jwt  /  oauth2 ），它负责调度。它不解决的问题包括： 

 同账号在第二台设备登录时，第一台应该被踢还是共存？用户被踢下线后，前端拿到 401，怎么区分"token 过期"和"管理员强制下线"？用户连续操作 24 小时不该被踢，但闲置 30 分钟应该自动登出——这两种过期机制怎么同时支持？除了  

**Lien**: [Lire](https://dev.to/pengcheng_e679693a21e1180/ba-sa-token-ban-dao-nestjs-sheng-tai-xlt-token-10-de-ji-ge-she-ji-qu-she-4017)
