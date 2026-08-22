---
layout: post
title: 'Tailscale Kernel TUN in Unprivileged LXC: Direct SSH Without Userspace Networking'
date: '2026-08-22'
category: tech-news
source: Dev.to
url: https://dev.to/futhgar/tailscale-kernel-tun-in-unprivileged-lxc-direct-ssh-without-userspace-networking-18la
tags:
- tech-news
- dev.to
---

## Tailscale Kernel TUN in Unprivileged LXC: Direct SSH Without Userspace Networking

**Source**: Dev.to

  tailscale up --tun=userspace-networking  gets you a green dot in the admin console and almost nothing else. The node appears in your tailnet,  tailscale status  looks healthy, and then you try to SSH into that container from your laptop and the connection hangs until TCP gives up. Two lines in the LXC config file fix it, and the container stays unprivileged. 

 That's the whole post, really. But those two lines only make sense once you understand why every guide pushes you toward userspace mod

**Lien**: [Lire](https://dev.to/futhgar/tailscale-kernel-tun-in-unprivileged-lxc-direct-ssh-without-userspace-networking-18la)
