---
title: "GHSA-prf8-cf2x-rhx7 — Maven org.hyperledger.fabric-sdk-java:fabric-sdk-java"
date: "2026-04-29"
layout: post
category: "advisory"
osv_id: "GHSA-prf8-cf2x-rhx7"
ecosystem: "Maven"
packages: ["org.hyperledger.fabric-sdk-java:fabric-sdk-java"]
cvss: 0
links: ["https://github.com/hyperledger/fabric/security/advisories/GHSA-prf8-cf2x-rhx7", "https://nvd.nist.gov/vuln/detail/CVE-2026-41586", "https://github.com/hyperledger/fabric-sdk-java", "https://hyperledger.github.io/fabric-gateway"]
tags: ["maven"]
---

fabric-sdk-java has ObjectInputStream.readObject() without ObjectInputFilter, which allows Java deserialization RCE

## References
- https://github.com/hyperledger/fabric/security/advisories/GHSA-prf8-cf2x-rhx7
- https://nvd.nist.gov/vuln/detail/CVE-2026-41586
- https://github.com/hyperledger/fabric-sdk-java
- https://hyperledger.github.io/fabric-gateway

