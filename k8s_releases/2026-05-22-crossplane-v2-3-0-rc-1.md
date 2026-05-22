---
layout: post
title: Crossplane v2.3.0-rc.1
date: '2026-05-22'
category: k8s-releases
tool: Crossplane
version: v2.3.0-rc.1
prerelease: true
url: https://github.com/crossplane/crossplane/releases/tag/v2.3.0-rc.1
tags:
- kubernetes
- cncf
- crossplane
---

## Crossplane v2.3.0-rc.1

**Version**: v2.3.0-rc.1
**Type**: Pre-release
**Release**: [https://github.com/crossplane/crossplane/releases/tag/v2.3.0-rc.1](https://github.com/crossplane/crossplane/releases/tag/v2.3.0-rc.1)

### Changelog

# ❗ Important

Crossplane version `v2.3.0-rc.1` is a release candidate intended to collect input from the community and offer users an opportunity to experiment with Crossplane in non-production environments before the official release of version `v2.3.0`.  

> [!WARNING]  
> This is a pre-release; do not use it in production environments!

To install Crossplane with this release:

```shell
helm repo add crossplane-stable https://charts.crossplane.io/stable --force-update
helm install crossplane --namespace crossplane-system --create-namespace crossplane-stable/crossplane --devel
```

# 🚨 Notable and Breaking Changes

* `github.com/crossplane/crossplane/apis/v2` is now a separate Go module from the rest of Crossplane. https://github.com/crossplane/crossplane/pull/7019
    
