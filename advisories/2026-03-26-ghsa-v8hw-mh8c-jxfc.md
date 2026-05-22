---
title: "GHSA-v8hw-mh8c-jxfc — PyPI langflow"
date: "2026-03-26"
layout: post
category: "advisory"
osv_id: "GHSA-v8hw-mh8c-jxfc"
ecosystem: "PyPI"
packages: ["langflow"]
cvss: 0
links: ["https://github.com/langflow-ai/langflow/security/advisories/GHSA-v8hw-mh8c-jxfc", "https://nvd.nist.gov/vuln/detail/CVE-2026-33873", "https://github.com/langflow-ai/langflow/blob/f7f4d1e70ba5eecd18162ec96f3571c2cfbcd1fc/src/lfx/src/lfx/services/settings/auth.py#L71-L87", "https://github.com/langflow-ai/langflow/blob/f7f4d1e70ba5eecd18162ec96f3571c2cfbcd1fc/src/lfx/src/lfx/custom/validate.py#L441-L443", "https://github.com/langflow-ai/langflow/blob/f7f4d1e70ba5eecd18162ec96f3571c2cfbcd1fc/src/lfx/src/lfx/custom/validate.py#L394-L399", "https://github.com/langflow-ai/langflow/blob/f7f4d1e70ba5eecd18162ec96f3571c2cfbcd1fc/src/lfx/src/lfx/custom/validate.py#L241-L272", "https://github.com/langflow-ai/langflow/blob/f7f4d1e70ba5eecd18162ec96f3571c2cfbcd1fc/src/backend/base/langflow/services/auth/utils.py#L39-L53", "https://github.com/langflow-ai/langflow/blob/f7f4d1e70ba5eecd18162ec96f3571c2cfbcd1fc/src/backend/base/langflow/services/auth/utils.py#L156-L163", "https://github.com/langflow-ai/langflow/blob/f7f4d1e70ba5eecd18162ec96f3571c2cfbcd1fc/src/backend/base/langflow/api/v1/login.py#L96-L135", "https://github.com/langflow-ai/langflow/blob/f7f4d1e70ba5eecd18162ec96f3571c2cfbcd1fc/src/backend/base/langflow/api/utils/core.py#L38", "https://github.com/langflow-ai/langflow/blob/f7f4d1e70ba5eecd18162ec96f3571c2cfbcd1fc/src/backend/base/langflow/agentic/services/assistant_service.py#L58-L79", "https://github.com/langflow-ai/langflow/blob/f7f4d1e70ba5eecd18162ec96f3571c2cfbcd1fc/src/backend/base/langflow/agentic/services/assistant_service.py#L259-L300", "https://github.com/langflow-ai/langflow/blob/f7f4d1e70ba5eecd18162ec96f3571c2cfbcd1fc/src/backend/base/langflow/agentic/services/assistant_service.py#L142-L156", "https://github.com/langflow-ai/langflow/blob/f7f4d1e70ba5eecd18162ec96f3571c2cfbcd1fc/src/backend/base/langflow/agentic/helpers/validation.py#L27-L47", "https://github.com/langflow-ai/langflow/blob/f7f4d1e70ba5eecd18162ec96f3571c2cfbcd1fc/src/backend/base/langflow/agentic/helpers/code_extraction.py#L11-L53", "https://github.com/langflow-ai/langflow/blob/f7f4d1e70ba5eecd18162ec96f3571c2cfbcd1fc/src/backend/base/langflow/agentic/api/schemas.py#L20-L31", "https://github.com/langflow-ai/langflow/blob/f7f4d1e70ba5eecd18162ec96f3571c2cfbcd1fc/src/backend/base/langflow/agentic/api/router.py#L252-L297", "https://github.com/langflow-ai/langflow"]
tags: ["pypi"]
---

Langflow has Authenticated Code Execution in Agentic Assistant Validation

## References
- https://github.com/langflow-ai/langflow/security/advisories/GHSA-v8hw-mh8c-jxfc
- https://nvd.nist.gov/vuln/detail/CVE-2026-33873
- https://github.com/langflow-ai/langflow/blob/f7f4d1e70ba5eecd18162ec96f3571c2cfbcd1fc/src/lfx/src/lfx/services/settings/auth.py#L71-L87
- https://github.com/langflow-ai/langflow/blob/f7f4d1e70ba5eecd18162ec96f3571c2cfbcd1fc/src/lfx/src/lfx/custom/validate.py#L441-L443
- https://github.com/langflow-ai/langflow/blob/f7f4d1e70ba5eecd18162ec96f3571c2cfbcd1fc/src/lfx/src/lfx/custom/validate.py#L394-L399
- https://github.com/langflow-ai/langflow/blob/f7f4d1e70ba5eecd18162ec96f3571c2cfbcd1fc/src/lfx/src/lfx/custom/validate.py#L241-L272
- https://github.com/langflow-ai/langflow/blob/f7f4d1e70ba5eecd18162ec96f3571c2cfbcd1fc/src/backend/base/langflow/services/auth/utils.py#L39-L53
- https://github.com/langflow-ai/langflow/blob/f7f4d1e70ba5eecd18162ec96f3571c2cfbcd1fc/src/backend/base/langflow/services/auth/utils.py#L156-L163
- https://github.com/langflow-ai/langflow/blob/f7f4d1e70ba5eecd18162ec96f3571c2cfbcd1fc/src/backend/base/langflow/api/v1/login.py#L96-L135
- https://github.com/langflow-ai/langflow/blob/f7f4d1e70ba5eecd18162ec96f3571c2cfbcd1fc/src/backend/base/langflow/api/utils/core.py#L38

