---
title: "Security Advisories Index (OSV)"
layout: default
permalink: /advisories/
---
# 🛡️ Security Advisories (OSV)
Agrégation automatique — PyPI, npm, Go, Maven, crates.io, RubyGems.
{% assign critical = site.advisories | where_exp: "item", "item.severity == 'CRITICAL'" | sort: "date" | reverse %}
{% assign high = site.advisories | where_exp: "item", "item.severity == 'HIGH'" | sort: "date" | reverse %}
{% if critical.size > 0 %}
### ⚠️ Critical ({{ critical.size }})
{% for p in critical limit:30 %}- **[{{ p.ecosystem }}]** <a href="{{ p.url | relative_url }}">{{ p.osv_id }}</a> — {{ p.date }}{% endfor %}
{% endif %}
{% if high.size > 0 %}
### 🔶 High ({{ high.size }})
{% for p in high limit:30 %}- **[{{ p.ecosystem }}]** <a href="{{ p.url | relative_url }}">{{ p.osv_id }}</a> — {{ p.date }}{% endfor %}
{% endif %}
Données: [OSV.dev](https://osv.dev) · Mise à jour quotidienne
