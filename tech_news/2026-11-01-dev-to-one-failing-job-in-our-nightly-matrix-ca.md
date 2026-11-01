---
layout: post
title: One failing job in our nightly matrix cancelled the eleven that would have
  told us more
date: '2026-11-01'
category: tech-news
source: Dev.to
url: https://dev.to/sergey_shinder_ab2d943365/one-failing-job-in-our-nightly-matrix-cancelled-the-eleven-that-would-have-told-us-more-350b
tags:
- tech-news
- dev.to
---

## One failing job in our nightly matrix cancelled the eleven that would have told us more

**Source**: Dev.to

 Our database client library supports four Postgres versions and three Python versions, and every night a GitHub Actions workflow runs the integration suite across all twelve combinations. In the week before the 3.0 release it failed five nights in a row, and every morning it reported exactly one broken job. 

 On Monday it was Python 3.10 against Postgres 13, a test matching the exact text of an error message that 3.10 had reworded. We fixed it. On Tuesday the same workflow failed on Python 3.1

**Lien**: [Lire](https://dev.to/sergey_shinder_ab2d943365/one-failing-job-in-our-nightly-matrix-cancelled-the-eleven-that-would-have-told-us-more-350b)
