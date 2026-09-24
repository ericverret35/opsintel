---
layout: post
title: 'Tag Confusion in the AWS Load Balancer Controller: How a K8s Developer Can
  Open Your Database to the Internet'
date: '2026-09-24'
category: tech-news
source: Dev.to
url: https://dev.to/bala_paranj_059d338e44e7e/tag-confusion-in-the-aws-load-balancer-controller-how-a-k8s-developer-can-open-your-database-to-144l
tags:
- tech-news
- dev.to
---

## Tag Confusion in the AWS Load Balancer Controller: How a K8s Developer Can Open Your Database to the Internet

**Source**: Dev.to

 
 ✓ Human-authored analysis; AI used for formatting and proofreading. 
 

 The AWS Load Balancer Controller manages security groups for ALBs on EKS. It identifies which security groups it owns using three tags: 
 

 
  elbv2.k8s.aws/cluster
ingress.k8s.aws/stack
ingress.k8s.aws/resource
  

 



 When it reconciles an Ingress resource, it queries EC2 for security groups matching those tags. If it finds one, it assumes ownership and applies the Ingress annotations as inbound rules. 

 Tags are n

**Lien**: [Lire](https://dev.to/bala_paranj_059d338e44e7e/tag-confusion-in-the-aws-load-balancer-controller-how-a-k8s-developer-can-open-your-database-to-144l)
