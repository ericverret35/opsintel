---
layout: post
title: 'When `@deprecated` cries wolf: Making Shopware’s next major upgrades easier'
date: '2026-08-25'
category: tech-news
source: Dev.to
url: https://dev.to/shopware/when-deprecated-cries-wolf-making-shopwares-next-major-upgrades-easier-983
tags:
- tech-news
- dev.to
---

## When `@deprecated` cries wolf: Making Shopware’s next major upgrades easier

**Source**: Dev.to

 When PHPStan reports that your extension calls a deprecated method, the expected next step is quite clear: find the replacement and migrate your code. 

 But what if there is no replacement? 

 Consider  Context::scope() . Previously, its planned change for Shopware 6.8 was announced like this: 
 

 
   /**
 * @deprecated tag:v6.8.0 - reason:new-optional-parameter - parameter $states will be added
 */ 
 public   function   scope  (  string   $scope  ,   \Closure   $callback  )  :   mixed 
  

 

**Lien**: [Lire](https://dev.to/shopware/when-deprecated-cries-wolf-making-shopwares-next-major-upgrades-easier-983)
