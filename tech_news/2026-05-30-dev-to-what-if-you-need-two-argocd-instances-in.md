---
layout: post
title: What If You Need Two ArgoCD Instances in One EKS Cluster?
date: '2026-05-30'
category: tech-news
source: Dev.to
url: https://dev.to/aws-builders/what-if-you-need-two-argocd-instances-in-one-eks-cluster-57id
tags:
- tech-news
- dev.to
---

## What If You Need Two ArgoCD Instances in One EKS Cluster?

**Source**: Dev.to

     

 Most ArgoCD tutorials start the same way: 

 Deploy ArgoCD. 

 Connect a Git repository. 

 Create an Application. 

 Done. 

 But what happens when multiple teams start sharing the same Kubernetes cluster? 

 Recently I was exploring a scenario where a single Amazon EKS cluster needed to support two different ArgoCD environments: 

 A Custom ArgoCD instance for the Platform Team 
A Managed ArgoCD instance for Application Teams 

 The Custom ArgoCD would manage infrastructure components 

**Lien**: [Lire](https://dev.to/aws-builders/what-if-you-need-two-argocd-instances-in-one-eks-cluster-57id)
