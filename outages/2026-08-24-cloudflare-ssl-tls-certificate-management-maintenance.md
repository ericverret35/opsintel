---
layout: post
title: SSL/TLS Certificate Management Maintenance
date: '2026-08-24'
vendor: Cloudflare
severity: incident
link: https://www.cloudflarestatus.com/incidents/n6lvrbqrkd5x
tags:
- cloudflare
- incident
---

<p><strong>THIS IS A SCHEDULED EVENT Aug <var>24</var>, <var>12:00</var> - <var>13:00</var> UTC</strong></p> <p> <small>Aug <var> 4</var>, <var>07:31</var> UTC</small><br /> <strong>Scheduled</strong> - Cloudflare will be performing scheduled maintenance on the databases that store SSL/TLS certificates, certificate orders, and related configuration. During this window, new certificate orders and renewals may be delayed or fail, and changes to SSL/TLS settings via the dashboard or API may experience elevated response times or temporary failures. This includes operations for Universal SSL, Advanced Certificate Manager (ACM), Total TLS, Custom Certificates, SSL for SaaS (custom hostnames), and Origin CA certificates. Cloudflare's edge will continue to proxy traffic and terminate TLS as normal, existing certificates will remain active and unaffected. Only new certificate operations and configuration changes are affected. </p>

More details: https://www.cloudflarestatus.com/incidents/n6lvrbqrkd5x
