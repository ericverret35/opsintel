---
layout: post
title: Cloudflare Workers Runtime API issues
date: '2026-08-04'
vendor: Cloudflare
severity: resolved
link: https://www.cloudflarestatus.com/incidents/238b69fw6l55
tags:
- cloudflare
- resolved
---

<p> <small>Aug <var> 4</var>, <var>07:12</var> UTC</small><br /> <strong>Resolved</strong> - This incident has been resolved. </p> <p> <small>Aug <var> 4</var>, <var>07:00</var> UTC</small><br /> <strong>Monitoring</strong> - A fix has been implemented and we are monitoring the results. </p> <p> <small>Aug <var> 3</var>, <var>15:21</var> UTC</small><br /> <strong>Identified</strong> - Workers runtime: Temporal global exposed with an incorrect clock<br /><br />Since 2026-07-30, the Workers runtime has exposed a global Temporal object that was not intended to be available. Its clock is wrong: Temporal.Now reports 1970-01-01 rather than the current time. Date and Date.now() are unaffected and report the correct time.<br /><br />This can affect Workers that install a Temporal polyfill only when no native Temporal is detected. On those Workers, the polyfill stopped being installed and time-dependent logic began computing against 1970 — for example, tokens minted with an issue time of 0 and an expiry in 1970, incorrect TTLs, or incorrect date arithmetic. No error is raised when this happens. </p> <p> <small>Aug <var> 3</var>, <var>15:13</var> UTC</small><br /> <strong>Investigating</strong> - Cloudflare is aware of an issue with the latest Workers Runtime API release that exposes native Temporal with clock stuck at epoch 0.  Updates to follow. </p>

More details: https://www.cloudflarestatus.com/incidents/238b69fw6l55
