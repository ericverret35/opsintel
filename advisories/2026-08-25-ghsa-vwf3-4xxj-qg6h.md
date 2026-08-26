---
title: "GHSA-vwf3-4xxj-qg6h — PyPI mcp-contextforge-gateway"
date: "2026-08-25"
layout: post
category: "advisory"
osv_id: "GHSA-vwf3-4xxj-qg6h"
ecosystem: "PyPI"
packages: ["mcp-contextforge-gateway"]
links: ["https://github.com/IBM/mcp-context-forge/security/advisories/GHSA-vwf3-4xxj-qg6h", "https://github.com/IBM/mcp-context-forge/issues/538", "https://github.com/IBM/mcp-context-forge/pull/4072", "https://github.com/IBM/mcp-context-forge/commit/4d31004661858a2e99055b3c0c9f14218b8f7120", "https://github.com/IBM/mcp-context-forge", "https://github.com/IBM/mcp-context-forge/releases/tag/v1.0.0"]
tags: ["pypi"]
---

mcp-contextforge-gateway has Server-Side Template Injection (SSTI) leading to Remote Code Execution in `PromptService._render_template` via unsandboxed Jinja2 Environment

## References
- https://github.com/IBM/mcp-context-forge/security/advisories/GHSA-vwf3-4xxj-qg6h
- https://github.com/IBM/mcp-context-forge/issues/538
- https://github.com/IBM/mcp-context-forge/pull/4072
- https://github.com/IBM/mcp-context-forge/commit/4d31004661858a2e99055b3c0c9f14218b8f7120
- https://github.com/IBM/mcp-context-forge
- https://github.com/IBM/mcp-context-forge/releases/tag/v1.0.0

