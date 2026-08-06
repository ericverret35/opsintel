---
layout: post
title: Maintenance for core backend database systems (cfdb)
date: '2026-08-29'
vendor: Cloudflare
severity: incident
link: https://www.cloudflarestatus.com/incidents/qwqw8lkssydy
tags:
- cloudflare
- incident
---

<p><strong>THIS IS A SCHEDULED EVENT Aug <var>29</var>, <var>08:55</var> - <var>11:05</var> UTC</strong></p> <p> <small>Aug <var> 5</var>, <var>08:57</var> UTC</small><br /> <strong>Scheduled</strong> - We will be performing scheduled maintenance on core backend database systems on 2026-08-29, in two back-to-back windows, as part of an ongoing database upgrade to improve performance, security, and reliability.<br /><br />09:00–10:00 UTC — Zone & account configuration: Configuration write operations made via the Dashboard, API, or tools such as Terraform may fail for up to 3 minutes. This includes:<br /><br />Zone management (creating, updating, deleting zones)<br />Zone settings (security level, SSL mode, caching, and other zone-level config)<br />SSL/TLS certificate management<br />Page Rules<br />Firewall Rules<br />Load Balancing configuration<br />10:00–11:00 UTC — Identity & access management (IAM): Configuration write operations made via the Dashboard or API may fail for up to 3 minutes. This includes:<br /><br />User & membership management (inviting or removing members)<br />Role & permission changes<br />API token & credential management (creating or revoking tokens and keys)<br />Resource Group changes<br />OAuth authorization & consent flows (granting third-party app access)<br />SSO & SCIM provisioning - automated user provisioning from your identity provider<br />The Cloudflare network will continue to proxy traffic and nameservers will continue to respond to DNS queries throughout this maintenance. Read-only operations, existing configurations, and existing access are not affected.<br /><br />We will post updates on this page before, during, and after each window. </p>

More details: https://www.cloudflarestatus.com/incidents/qwqw8lkssydy
