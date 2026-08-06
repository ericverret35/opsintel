---
layout: post
title: 低遅延の打鍵音をAVAudioPlayerNodeプールで重ねる設計
date: '2026-08-06'
category: tech-news
source: Dev.to
url: https://dev.to/klakkapp/di-chi-yan-noda-jian-yin-woavaudioplayernodepurudezhong-nerushe-ji-2hc1
tags:
- tech-news
- dev.to
---

## 低遅延の打鍵音をAVAudioPlayerNodeプールで重ねる設計

**Source**: Dev.to

 Macでキー入力に合わせて短い効果音を鳴らすとき、毎回ファイルを開いてプレイヤーを作ると、入力のホットパスにI/Oと初期化が入り込みます。この記事では、私が有料macOSアプリKlakkで使っている現在の構成を題材に、 事前準備したPCMバッファ と AVAudioPlayerNodeの固定プール をどう分けたかを整理します。 

 
  
  
  1. キー入力より前に音を準備する
 

 再生時に必要なのは、キーコードからすでに変換済みのバッファを引くことだけにします。 
 

 
   private   struct   PreparedKeySound   { 
     let   buffer  :   AVAudioPCMBuffer 
     let   outputGain  :   Float 
 } 

 private   var   preparedKeySounds  :   [  String  :   PreparedKeySound  ]   =   [:] 
 private   let   stateLock   =   NSLock  (

**Lien**: [Lire](https://dev.to/klakkapp/di-chi-yan-noda-jian-yin-woavaudioplayernodepurudezhong-nerushe-ji-2hc1)
