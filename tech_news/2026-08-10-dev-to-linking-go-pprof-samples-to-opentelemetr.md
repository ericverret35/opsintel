---
layout: post
title: Linking Go pprof Samples to OpenTelemetry Traces with OTLP Profiles
date: '2026-08-10'
category: tech-news
source: Dev.to
url: https://dev.to/trknhr/linking-go-pprof-samples-to-opentelemetry-traces-with-otlp-profiles-1mf0
tags:
- tech-news
- dev.to
---

## Linking Go pprof Samples to OpenTelemetry Traces with OTLP Profiles

**Source**: Dev.to

 Traces tell us which request was slow. CPU profiles tell us which functions consumed CPU time. 

 Can we start from a slow span and open only the CPU profile samples captured while that span was running? 

 This article explores that question by converting Go's built-in pprof data into OTLP Profiles, then linking individual Profile Samples to OpenTelemetry Trace and Span IDs. The final result is a Grafana workflow that starts from a  GET /cpu-heavy  span and opens a Pyroscope flame graph contai

**Lien**: [Lire](https://dev.to/trknhr/linking-go-pprof-samples-to-opentelemetry-traces-with-otlp-profiles-1mf0)
