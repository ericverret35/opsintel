---
title: "GHSA-hvqh-jw65-wcpq — npm devbridge-autocomplete"
date: "2026-06-22"
layout: post
category: "advisory"
osv_id: "GHSA-hvqh-jw65-wcpq"
ecosystem: "npm"
packages: ["devbridge-autocomplete"]
cvss: 0
links: ["https://github.com/devbridge/jQuery-Autocomplete/security/advisories/GHSA-hvqh-jw65-wcpq", "https://github.com/devbridge/jQuery-Autocomplete/commit/63ff096ff5b77a90aac7fb5dad7c86e538a59ce0", "https://github.com/devbridge/jQuery-Autocomplete"]
tags: ["npm"]
---

devbridge-autocomplete has XSS in its default formatters: formatGroup and formatResult fail to escape HTML in untrusted inputs

## References
- https://github.com/devbridge/jQuery-Autocomplete/security/advisories/GHSA-hvqh-jw65-wcpq
- https://github.com/devbridge/jQuery-Autocomplete/commit/63ff096ff5b77a90aac7fb5dad7c86e538a59ce0
- https://github.com/devbridge/jQuery-Autocomplete

