title: "Security Advisories Index (OSV)"
layout: default
permalink: /advisories/
Security Advisories (OSV)
Agregation automatique — PyPI, npm, Go, Maven, crates.io, RubyGems.

{% if site.advisories and site.advisories.size > 0 %}

{% assign critical = site.advisories | where_exp: "item", "item.severity == 'CRITICAL'" | sort: "date" | reverse %}
{% assign high = site.advisories | where_exp: "item", "item.severity == 'HIGH'" | sort: "date" | reverse %}

{% if critical.size > 0 %}

Critical ({{ critical.size }})
{% for p in critical limit:30 %}

[{{ p.ecosystem }}] <a href="{{ p.url | relative_url }}">{{ p.osv_id }}</a> — {{ p.date }}
{% endfor %}
{% endif %}
{% if high.size > 0 %}

High ({{ high.size }})
{% for p in high limit:30 %}

[{{ p.ecosystem }}] <a href="{{ p.url | relative_url }}">{{ p.osv_id }}</a> — {{ p.date }}
{% endfor %}
{% endif %}
{% else %}
No advisories available yet. Content updates daily at 06:00 UTC.
{% endif %}

Donnees: OSV.dev - Mise a jour quotidienne
