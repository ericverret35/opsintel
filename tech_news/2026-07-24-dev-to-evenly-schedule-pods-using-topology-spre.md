---
layout: post
title: Evenly schedule pods using Topology Spread Constraints in AWS EKS
date: '2026-07-24'
category: tech-news
source: Dev.to
url: https://dev.to/aws-builders/evenly-schedule-pods-using-topology-spread-constraints-in-aws-eks-g8k
tags:
- tech-news
- dev.to
---

## Evenly schedule pods using Topology Spread Constraints in AWS EKS

**Source**: Dev.to

 The Kubernetes Topology Spread Constraints allow scheduling pods evenly across nodes, regions and availability zones.  

 The following TopologySpreadConstraints ensure that at any given time, the difference in the number of pods between two nodes never exceeds 2. 

 Instance: If you run 5 pods on 3 nodes. Kubernetes scheduler will schedule them as either  1:1:3  or  2:2:1  based on  topologyKey: kubernetes.io/hostname  
 

 
  option 1: Maximum difference is 3-1=2
option 2: Maximum difference 

**Lien**: [Lire](https://dev.to/aws-builders/evenly-schedule-pods-using-topology-spread-constraints-in-aws-eks-g8k)
