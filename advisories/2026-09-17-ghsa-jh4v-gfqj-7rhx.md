---
title: "GHSA-jh4v-gfqj-7rhx — Maven com.rabbitmq:amqp-client"
date: "2026-09-17"
layout: post
category: "advisory"
osv_id: "GHSA-jh4v-gfqj-7rhx"
ecosystem: "Maven"
packages: ["com.rabbitmq:amqp-client"]
cvss: 0
links: ["https://github.com/rabbitmq/rabbitmq-java-client/security/advisories/GHSA-jh4v-gfqj-7rhx", "https://nvd.nist.gov/vuln/detail/CVE-2026-75516", "https://github.com/rabbitmq/rabbitmq-java-client/pull/2015", "https://github.com/rabbitmq/rabbitmq-java-client/pull/2016", "https://github.com/rabbitmq/rabbitmq-java-client/commit/6d7c2bfe89796ca34d3531098fb59dd657fea39e", "https://github.com/rabbitmq/rabbitmq-java-client/commit/e7f10bf99aee103dd9f64b3e52a725fc9f9d3763", "https://github.com/rabbitmq/rabbitmq-java-client", "https://github.com/rabbitmq/rabbitmq-java-client/releases/tag/v5.34.0"]
tags: ["maven"]
---

RabbitMQ Java client has frame-level OOM: Math.min(maxInboundMessageBodySize, 0) defeats frame size enforcement

## References
- https://github.com/rabbitmq/rabbitmq-java-client/security/advisories/GHSA-jh4v-gfqj-7rhx
- https://nvd.nist.gov/vuln/detail/CVE-2026-75516
- https://github.com/rabbitmq/rabbitmq-java-client/pull/2015
- https://github.com/rabbitmq/rabbitmq-java-client/pull/2016
- https://github.com/rabbitmq/rabbitmq-java-client/commit/6d7c2bfe89796ca34d3531098fb59dd657fea39e
- https://github.com/rabbitmq/rabbitmq-java-client/commit/e7f10bf99aee103dd9f64b3e52a725fc9f9d3763
- https://github.com/rabbitmq/rabbitmq-java-client
- https://github.com/rabbitmq/rabbitmq-java-client/releases/tag/v5.34.0

