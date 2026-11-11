---
layout: post
title: Java 类和对象（二）：包、封装、static 与代码块
date: '2026-11-11'
category: tech-news
source: Dev.to
url: https://dev.to/homlander_7c7851e210d2a/java-lei-he-dui-xiang-er-bao-feng-zhuang-static-yu-dai-ma-kuai-50fp
tags:
- tech-news
- dev.to
---

## Java 类和对象（二）：包、封装、static 与代码块

**Source**: Dev.to

 
  
  
  1. 包：给类分类，也给类名加上范围
 

 项目中的类越来越多时，需要按用途组织；不同地方也可能出现同名的类。 包（package）用来组织类，并区分不同包中的同名类。  

 例如， java.util.Date  和  java.sql.Date  都叫  Date ，但它们属于不同的包，是两个不同的类。 包名.类名  称为类的 全限定名 。 

 
  
  
  1.1 声明包与创建目录
 

  package  表示“当前源文件中的类属于哪个包”，放在源文件开头、 import  和类定义之前；前面可以有注释。 
 

 
   package   com  .  bit  .  demo1  ; 

 public   class   Test   { 
     public   static   void   main  (  String  [  ]   args  )   { 
         System  .  out  .  println  (  "Hello"  )  ; 
     } 
 } 
  

 



 在 IDEA

**Lien**: [Lire](https://dev.to/homlander_7c7851e210d2a/java-lei-he-dui-xiang-er-bao-feng-zhuang-static-yu-dai-ma-kuai-50fp)
