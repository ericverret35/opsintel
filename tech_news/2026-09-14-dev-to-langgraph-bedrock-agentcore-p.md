---
layout: post
title: LangGraph 에이전트를 Bedrock AgentCore로 이관한 PoC 후기
date: '2026-09-14'
category: tech-news
source: Dev.to
url: https://dev.to/janus/langgraph-eijeonteureul-bedrock-agentcorero-igwanhan-poc-hugi-3pmh
tags:
- tech-news
- dev.to
---

## LangGraph 에이전트를 Bedrock AgentCore로 이관한 PoC 후기

**Source**: Dev.to

     

 주말에  Migrate agentic workloads to Amazon Bedrock AgentCore  글을 읽었는데, 문장 하나가 눈에 박혔습니다. "노트북에서 돌아가는 에이전트는 프로덕션 에이전트가 아니다." 정확히 지난 분기에 겪은 상황이었습니다. LangGraph로 만든 고객 지원 에이전트 데모는 잘 돌아갔는데, 실사용자가 붙기 시작하니 세션 격리, 체크포인트 지속성, 툴 인증 같은 것들이 전부 우리 코드가 되어버렸거든요. 

 Amazon Bedrock AgentCore는 이 "에이전트 추론과 상관없는 운영 부담"을 서비스 단위로 떼어가는 플랫폼입니다. Runtime은 세션당 마이크로VM으로 컴퓨트를 대신 돌려주고, Gateway는 툴을 MCP(Model Context Protocol)로 퍼블리싱하면서 인증을 대신 처리하고, Memory는 프로세스가 죽어도 대화 상태를 유지합니다. 원문에서는 이 세 가지를 붙이는 걸 Stage 1, 루프 자체를 모델 주도 

**Lien**: [Lire](https://dev.to/janus/langgraph-eijeonteureul-bedrock-agentcorero-igwanhan-poc-hugi-3pmh)
