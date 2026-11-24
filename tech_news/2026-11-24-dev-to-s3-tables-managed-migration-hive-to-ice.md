---
layout: post
title: 'S3 Tables Managed Migration: Hive to Iceberg Without Writing a Pipeline'
date: '2026-11-24'
category: tech-news
source: Dev.to
url: https://dev.to/damogallagher/s3-tables-managed-migration-hive-to-iceberg-without-writing-a-pipeline-11g0
tags:
- tech-news
- dev.to
---

## S3 Tables Managed Migration: Hive to Iceberg Without Writing a Pipeline

**Source**: Dev.to

 If you still have Hive tables sitting in the Glue Data Catalog as Parquet, S3 Tables now has a managed way to turn them into Iceberg tables. It went out on 4 November. Here's how it works and where it stops. 




 
  
  
  The workflow
 

 The migration has three steps: Start, Sync, Complete. 

 
 
 Start  creates the destination Iceberg table in a table bucket and copies the data. 
 
 Sync  can be run as many times as you like, to pick up changes to the source before you cut over. 
 
 Complete

**Lien**: [Lire](https://dev.to/damogallagher/s3-tables-managed-migration-hive-to-iceberg-without-writing-a-pipeline-11g0)
