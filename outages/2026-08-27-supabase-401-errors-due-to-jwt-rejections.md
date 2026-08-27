---
layout: post
title: 401 errors due to JWT rejections
date: '2026-08-27'
vendor: Supabase
severity: resolved
link: https://status.supabase.com/incidents/6q5902p2xd9f
tags:
- supabase
- resolved
---

<p> <small>Aug <var>27</var>, <var>17:17</var> UTC</small><br /> <strong>Update</strong> - PostgREST 14.17 has now been rolled out to all regions. <br />Some customers have reported that restarting their project after the rollout resolved this issue.<br />To restart your project, go to the General settings page in the dashboard and select Restart project. <br />Please contact our support team if the issue persists after a restart. </p> <p> <small>Aug <var>25</var>, <var>18:41</var> UTC</small><br /> <strong>Update</strong> - We are continuing to rollout the fixes for intermittent HTTP 401 errors. In most cases, waiting and refreshing is successful. <br /><br />This fix has been applied to the following regions: <br />ap-east-1<br />ap-northeast-1<br />ap-northeast-2<br />ap-south-1<br />ap-southeast-1<br />ap-southeast-2<br />ca-central-1<br />eu-central-1<br />eu-central-2<br />eu-north-1<br />eu-west-2<br />eu-west-3<br /><br />We will continue rolling out this fix to the remaining regions throughout this week and provide updates as more regions are successful. </p> <p> <small>Aug <var>21</var>, <var>17:21</var> UTC</small><br /> <strong>Update</strong> - We are continuing to test and rollout the fixes for intermittent HTTP 401 errors. In most cases, waiting and refreshing is successful. <br /><br />We will monitor eu-central-2 over the weekend and are preparing for the fix to be pushed to all regions starting Monday. Thank you for your patience while we've worked on multiple fixes for this issue. </p> <p> <small>Aug <var>20</var>, <var>16:37</var> UTC</small><br /> <strong>Update</strong> - As part of the incident remediation flow, we have separately identified "/lib/aarch64-linux-gnu/libc.so.6: version `GLIBC_2.34' not found" error between 11:15 - 16:24 UTC today affecting PostgREST. This has been fixed and we can see the error rates have subsided. </p> <p> <small>Aug <var>18</var>, <var>18:38</var> UTC</small><br /> <strong>Update</strong> - Fixes for this issu

More details: https://status.supabase.com/incidents/6q5902p2xd9f
