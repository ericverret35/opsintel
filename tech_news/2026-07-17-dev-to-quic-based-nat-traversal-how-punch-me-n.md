---
layout: post
title: 'QUIC-Based NAT Traversal: How PUNCH_ME_NOW Frames Are Standardizing Hole Punching'
date: '2026-07-17'
category: tech-news
source: Dev.to
url: https://dev.to/mannansaood_83/quic-based-nat-traversal-how-punchmenow-frames-are-standardizing-hole-punching-2969
tags:
- tech-news
- dev.to
---

## QUIC-Based NAT Traversal: How PUNCH_ME_NOW Frames Are Standardizing Hole Punching

**Source**: Dev.to

  TL;DR:  NAT traversal has historically relied on STUN/TURN/ICE running as an external signalling layer bolted onto whatever transport protocol you choose. A 2023 IETF draft by Marten Seemann ( draft-seemann-quic-nat-traversal ) proposes something different: use QUIC's own path validation mechanism, extended with three new frames ( ADD_ADDRESS ,  PUNCH_ME_NOW ,  REMOVE_ADDRESS ), to punch holes and migrate to direct paths natively. A 2024 measurement study confirms the theory that QUIC hole pun

**Lien**: [Lire](https://dev.to/mannansaood_83/quic-based-nat-traversal-how-punchmenow-frames-are-standardizing-hole-punching-2969)
