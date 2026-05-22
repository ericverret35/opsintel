---
layout: post
title: Upgrade Shared Pooler V1 to V2 for us-west-1 region
date: '2026-05-28'
vendor: Supabase
severity: incident
link: https://status.supabase.com/incidents/8f72bnv3xs8r
tags:
- supabase
- incident
---

<p><strong>THIS IS A SCHEDULED EVENT May <var>28</var>, <var>16:00</var> - <var>18:00</var> UTC</strong></p><p><small>May <var>18</var>, <var>02:55</var> UTC</small><br /><strong>Scheduled</strong> - There will be scheduled maintenance on 2026-05-28 from 16:00-18:00 UTC (09:00-11:00 PDT) on the Shared Pooler(V1) for the us-west-1 region.<br /><br />This maintenance upgrades the Shared Pooler to a new version (V2) that provides better scalability and uptime.<br /><br />The Shared Pooler will be unavailable during this time period for anyone connecting to their projects using it. Your projects remain available and connections via the Dedicated Pooler and Direct Connections will continue to work. <br /><br />How to determine whether you are affected:<br /><br />Only projects connecting to V1 of the Shared Pooler are affected. If your connection string has the format:<br /><br />aws-0-us-west-1-pooler.supabase.com, you can expect to see errors during the maintenance.<br /><br />Those using connection strings with the format: aws-us-west-1.pooler.supabase.comare not affected by this maintenance.<br /><br />Please follow the status page for updates.</p>

More details: https://status.supabase.com/incidents/8f72bnv3xs8r
