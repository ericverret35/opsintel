---
layout: post
title: 'Artifact Immutability as a Release Primitive: Content Addressing, Digest Pinning,
  and the Substitution Attack Surface'
date: '2026-11-12'
category: tech-news
source: Dev.to
url: https://dev.to/neeraj_singhi_golang/artifact-immutability-as-a-release-primitive-content-addressing-digest-pinning-and-the-168n
tags:
- tech-news
- dev.to
---

## Artifact Immutability as a Release Primitive: Content Addressing, Digest Pinning, and the Substitution Attack Surface

**Source**: Dev.to

 
  
  
  Artifact Immutability as a Release Primitive: Content Addressing, Digest Pinning, and the Substitution Attack Surface
 

 Most teams treat image tags as release identifiers. They are not. A tag is a mutable pointer sitting on top of a content-addressed blob store. The digest— sha256:&lt;64-hex&gt; —is the identifier. Conflating the two produces a class of failure that looks like a deployment problem but is actually an artifact provenance problem: the rollback you thought was safe pulle

**Lien**: [Lire](https://dev.to/neeraj_singhi_golang/artifact-immutability-as-a-release-primitive-content-addressing-digest-pinning-and-the-168n)
