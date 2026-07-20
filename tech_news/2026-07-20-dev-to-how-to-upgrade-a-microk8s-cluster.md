---
layout: post
title: How to upgrade a MicroK8s cluster
date: '2026-07-20'
category: tech-news
source: Dev.to
url: https://dev.to/sertxudev/how-to-upgrade-a-microk8s-cluster-3pib
tags:
- tech-news
- dev.to
---

## How to upgrade a MicroK8s cluster

**Source**: Dev.to

 For this tutorial, we'll use a 3-node MicroK8s cluster with nodes k8s-1, k8s-2, and k8s-3. 
 

 
  microk8s kubectl get nodes
  

 





 
  NAME    STATUS   ROLES    AGE    VERSION
k8s-1   Ready    &lt;none&gt;   142d   v1.35.6
k8s-2   Ready    &lt;none&gt;   142d   v1.35.6
k8s-3   Ready    &lt;none&gt;   142d   v1.35.6
  

 



 
  
  
  Upgrade the first node
 

 To upgrade a node, we must cordon it first so new pods cannot be scheduled on it. 
 

 
  microk8s kubectl cordon k8s-1
  

 






**Lien**: [Lire](https://dev.to/sertxudev/how-to-upgrade-a-microk8s-cluster-3pib)
