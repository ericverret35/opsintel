---
title: "GHSA-qv8h-rqr3-mph9 — Maven org.silverpeas.core:silverpeas-core-war"
date: "2026-06-10"
layout: post
category: "advisory"
osv_id: "GHSA-qv8h-rqr3-mph9"
ecosystem: "Maven"
packages: ["org.silverpeas.core:silverpeas-core-war", "org.silverpeas.core:silverpeas-core"]
cvss: 0
links: ["https://nvd.nist.gov/vuln/detail/CVE-2026-53698", "https://github.com/Silverpeas/Silverpeas-Core/commit/caa6e6d1ac967ebd29b39e11c2ef5e7fd0047eec", "https://github.com/Silverpeas/Silverpeas-Core", "https://github.com/Silverpeas/Silverpeas-Core/blob/983c5d07928b8a5ddcb39cc17d7fb9a0d87019b9/core-war/src/main/java/org/silverpeas/web/servlets/FileServer.java#L120-L122", "https://github.com/Silverpeas/Silverpeas-Core/blob/983c5d07928b8a5ddcb39cc17d7fb9a0d87019b9/core-war/src/main/java/org/silverpeas/web/servlets/FileServer.java#L150-L153", "https://github.com/Silverpeas/Silverpeas-Core/releases/tag/6.4.7", "https://tracker.silverpeas.org/issues/15229"]
tags: ["maven"]
---

Silverpeas mishandles the "Personal space" feature that is selected when no componentId is set

## References
- https://nvd.nist.gov/vuln/detail/CVE-2026-53698
- https://github.com/Silverpeas/Silverpeas-Core/commit/caa6e6d1ac967ebd29b39e11c2ef5e7fd0047eec
- https://github.com/Silverpeas/Silverpeas-Core
- https://github.com/Silverpeas/Silverpeas-Core/blob/983c5d07928b8a5ddcb39cc17d7fb9a0d87019b9/core-war/src/main/java/org/silverpeas/web/servlets/FileServer.java#L120-L122
- https://github.com/Silverpeas/Silverpeas-Core/blob/983c5d07928b8a5ddcb39cc17d7fb9a0d87019b9/core-war/src/main/java/org/silverpeas/web/servlets/FileServer.java#L150-L153
- https://github.com/Silverpeas/Silverpeas-Core/releases/tag/6.4.7
- https://tracker.silverpeas.org/issues/15229

