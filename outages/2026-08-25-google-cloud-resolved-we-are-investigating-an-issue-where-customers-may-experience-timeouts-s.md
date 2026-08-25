---
layout: post
title: 'RESOLVED: We are investigating an issue where customers may experience timeouts,
  service degradations, errors, and elevated latencies across multiple products in
  the us-west1 region.'
date: '2026-08-25'
vendor: Google Cloud
severity: partial
link: https://status.cloud.google.com/incidents/utF3FMFdQfwBzJcGG6vf
tags:
- google cloud
- partial
---

<p> Incident began at <strong>2026-08-20 08:40</strong> and ended at <strong>2026-08-20 12:20</strong> <span>(all times are <strong>US/Pacific</strong>).</span></p><div class="cBIRi14aVDP__status-update-text"><h1>Preliminary Incident Report</h1>
<p>We sincerely apologize for the disruption this incident caused to your business operations. Recognizing your reliance on Google Cloud, we express our sincere regrets for any operational impact experienced. Our engineering teams are actively addressing the underlying root cause to prevent future recurrences.</p>
<p>Please note that the information provided herein reflects our current understanding as of the time of publication and remains subject to revision as the investigation progresses. A comprehensive Incident Report detailing preventive measures will be issued upon conclusion of our inquiry.</p>
<p>If you have experienced impact outside of what is listed below, please reach out to Google Cloud Support using <a href="https://cloud.google.com/support">https://cloud.google.com/support</a>.</p>
<h2>Date/Time of the Issue (All time US/Pacific)</h2>
<ul>
<li>Incident Start: 20 August 2026 08:00</li>
<li>Incident End: 20 August 2026 10:22</li>
<li>Duration: 2 hours, 22 minutes</li>
</ul>
<h2>Summary</h2>
<p>On Thursday, 20 August 2026, multiple Google Cloud services encountered elevated latency, provisioning failures, increased error rates, and service degradations lasting for a duration of 2 hours and 22 minutes.</p>
<h2>Preliminary Root Cause</h2>
<p>The disruption originated during scheduled fiber optic maintenance, which unexpectedly compromised network capacity between data centers within the us-west1 region. Automated rerouting mechanisms failed to properly redistribute traffic to alternate capacity, resulting in network congestion as volumes exceeded available bandwidth in the affected area.</p>
<p>This underlying network degradation subsequently impacted higher-level service components through request throttling, in

More details: https://status.cloud.google.com/incidents/utF3FMFdQfwBzJcGG6vf
