---
layout: post
title: Zero Trust Underlying Storage Maintenance
date: '2026-06-18'
vendor: Cloudflare
severity: incident
link: https://www.cloudflarestatus.com/incidents/9kk07jfry9rf
tags:
- cloudflare
- incident
---

<p><strong>THIS IS A SCHEDULED EVENT Jun <var>18</var>, <var>12:00</var> - <var>13:00</var> UTC</strong></p> <p> <small>Jun <var>12</var>, <var>00:38</var> UTC</small><br /> <strong>Scheduled</strong> - Cloudflare has scheduled maintenance for the backend storage system supporting Cloudflare One Client (WARP) / Zero Trust device management. Services will continue to operate normally. During a brief window of up to 3 minutes, device-related settings will be read-only: customers will be unable to enroll new devices, or create/modify/revoke/delete device registrations, device settings, device profiles, device posture rules, third-party posture integrations, managed networks, WARP deployment groups, and egress/IP profiles (via the Zero Trust dashboard or the public API). This restriction includes all dashboard edits and API write calls. New WARP device and WARP Connector enrollments will also fail to complete during that brief period.<br /><br />Traffic will not be affected. Already enrolled devices will be able to connect/disconnect as normal. Switching device profiles based on managed networks will be unavailable.<br /><br />The following services will experience configuration and new-enrollment limitations during this window:<br />Cloudflare One Client (new device enrollment)<br />Cloudflare Mesh (new device enrollment)<br />Zero Trust device management (public API, dashboard)<br />Device posture integrations with third-parties will be delayed </p>

More details: https://www.cloudflarestatus.com/incidents/9kk07jfry9rf
