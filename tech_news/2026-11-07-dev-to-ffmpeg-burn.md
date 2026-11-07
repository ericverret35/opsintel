---
layout: post
title: वर्टिकल वीडियो पर ffmpeg से burn किए सबटाइटल गलत जगह क्यों आते हैं?
date: '2026-11-07'
category: tech-news
source: Dev.to
url: https://dev.to/bestaitools-hi/vrttikl-viiddiyo-pr-ffmpeg-se-burn-kie-sbttaaittl-glt-jgh-kyon-aate-hain-29n
tags:
- tech-news
- dev.to
---

## वर्टिकल वीडियो पर ffmpeg से burn किए सबटाइटल गलत जगह क्यों आते हैं?

**Source**: Dev.to

 TikTok या Reels के लिए 1080×1920 वीडियो में कैप्शन burn करते समय शुरुआत आमतौर पर एक समझदारी भरे प्लान से होती है: फ़ीड फ्रेम के नीचे का करीब पाँचवाँ हिस्सा ढक लेती है, तो कैप्शन उसके ऊपर रखो। ffmpeg के  subtitles  फ़िल्टर के साथ आप  force_style  लेते हैं और  MarginV  सेट करते हैं। फिर रेंडर करते हैं, और कैप्शन किसी बिल्कुल दूसरी जगह होता है, और उम्मीद से कहीं बड़ा। 

 वजह यह है कि  .srt  फ़ाइल को पता ही नहीं होता कि आपका वीडियो कितना बड़ा है। ffmpeg उसे एक तय और बहुत छोटे canvas वाली ASS script

**Lien**: [Lire](https://dev.to/bestaitools-hi/vrttikl-viiddiyo-pr-ffmpeg-se-burn-kie-sbttaaittl-glt-jgh-kyon-aate-hain-29n)
