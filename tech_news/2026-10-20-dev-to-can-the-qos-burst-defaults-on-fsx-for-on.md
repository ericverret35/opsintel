---
layout: post
title: Can the QoS burst defaults on FSx for ONTAP be changed from ONTAP 9.19.1, the
  same as on-premises? I checked on a live file system
date: '2026-10-20'
category: tech-news
source: Dev.to
url: https://dev.to/aws-builders/can-the-qos-burst-defaults-on-fsx-for-ontap-be-changed-from-ontap-9191-the-same-as-on-premises-2ce7
tags:
- tech-news
- dev.to
---

## Can the QoS burst defaults on FSx for ONTAP be changed from ONTAP 9.19.1, the same as on-premises? I checked on a live file system

**Source**: Dev.to

 Conclusion first: on Amazon FSx for NetApp ONTAP you can change the QoS burst defaults. Not only is the configuration accepted — a brief overshoot above the ceiling (the burst) happened exactly as configured. The catch: you cannot change this setting from the AWS Management Console or the AWS CLI (the AWS API). FSx for ONTAP has two ways in — the AWS-side consoles and APIs, and a separate path that drives the storage engine (ONTAP) directly through its own REST API / CLI. The QoS burst can be s

**Lien**: [Lire](https://dev.to/aws-builders/can-the-qos-burst-defaults-on-fsx-for-ontap-be-changed-from-ontap-9191-the-same-as-on-premises-2ce7)
