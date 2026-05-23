---
layout: post
title: Upgrade Shared Pooler V1 to V2 for eu-west-1 region
date: '2026-06-01'
vendor: Supabase
severity: incident
link: https://status.supabase.com/incidents/3t293hpd545z
tags:
- supabase
- incident
---

<p><strong>THIS IS A SCHEDULED EVENT Jun <var>1</var>, <var>13:00</var> - <var>15:00</var> UTC</strong></p> <p> <small>May <var>18</var>, <var>02:52</var> UTC</small><br /> <strong>Scheduled</strong> - There will be a scheduled maintenance on 2026-06-01 from 13:00-15:00 UTC on the Shared Pooler(V1) for the eu-west-1 region.<br /><br />This maintenance upgrades the Shared Pooler to a new version (V2) that provides better scalability and uptime.<br /><br />The Shared Pooler will be unavailable during this time period for anyone connecting to their projects using it. Your projects remain available and connections via the Dedicated Pooler and Direct Connections will continue to work. <br /><br />How to determine whether you are affected:<br /><br />Only projects connecting to V1 of the Shared Pooler are affected. If your connection string has the format:<br /><br />aws-0-eu-west-1-pooler.supabase.com, you can expect to see errors during the maintenance.<br /><br />Those using connection strings with the format: aws-eu-west-1.pooler.supabase.com are not affected by this maintenance.<br /><br />Please follow the status page for updates. </p>

More details: https://status.supabase.com/incidents/3t293hpd545z
