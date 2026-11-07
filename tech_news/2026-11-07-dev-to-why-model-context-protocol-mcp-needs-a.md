---
layout: post
title: Why Model Context Protocol (MCP) Needs an Execution Firewall (And How We're
  Experimenting with One in Rust)
date: '2026-11-07'
category: tech-news
source: Dev.to
url: https://dev.to/fcn06/why-model-context-protocol-mcp-needs-an-execution-firewall-and-how-were-experimenting-with-one-29af
tags:
- tech-news
- dev.to
---

## Why Model Context Protocol (MCP) Needs an Execution Firewall (And How We're Experimenting with One in Rust)

**Source**: Dev.to

 
  TL;DR:  The Model Context Protocol (MCP) is solving one of the hardest developer problems in AI: giving models a standard way to find tools and context. But once an agent selects a tool, execution is usually direct: the agent calls the tool with standing API credentials. If an LLM hallucinates, misreads a number, or gets tricked by a prompt injection, nothing stands in between. We're experimenting with an inline zero-trust proxy written in Rust that treats agent tool calls as untrusted propo

**Lien**: [Lire](https://dev.to/fcn06/why-model-context-protocol-mcp-needs-an-execution-firewall-and-how-were-experimenting-with-one-29af)
