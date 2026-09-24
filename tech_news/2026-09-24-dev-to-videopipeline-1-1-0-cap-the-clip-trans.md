---
layout: post
title: 'VideoPipeline 1.1.0: Cap the Clip, Transcode on the OS, Then Encrypt'
date: '2026-09-24'
category: tech-news
source: Dev.to
url: https://dev.to/niladri_prasadpadhy_ccee/videopipeline-110-cap-the-clip-transcode-on-the-os-then-encrypt-11d9
tags:
- tech-news
- dev.to
---

## VideoPipeline 1.1.0: Cap the Clip, Transcode on the OS, Then Encrypt

**Source**: Dev.to

 A 40-second 4K clip should not leave the device at full size. The app needs a duration cap, a smaller frame, a thumbnail, and a file it can encrypt before upload. 

  Plugin.Maui.VideoPipeline  is that path. Version  1.1.0  is on nuget.org.  FromCamera  and  FromGallery  pick the clip.  MaxDuration ,  MaxResolution , and  MaxBytes  are the gates. Over budget, the plugin asks the OS encoder to shrink it. If the device cannot encode, the result is  CannotTranscode . There is no FFmpeg binary in t

**Lien**: [Lire](https://dev.to/niladri_prasadpadhy_ccee/videopipeline-110-cap-the-clip-transcode-on-the-os-then-encrypt-11d9)
