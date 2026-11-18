# 모모콜 플러그인

모모콜 앱의 통화기록·요약·일정·할 일을 AI 에이전트에서 불러와 업무를 돕는 플러그인입니다.

## 설치 (Claude Code)

```text
/plugin install momocall --marketplace cashcall-team/momocall-plugins
```

설치 후 `/mcp` → `momocall` → **Authenticate**로 모모콜 계정을 연결합니다.

## 들어 있는 것

- 원격 MCP 서버 연결: `https://mcp.momocall.kr/mcp`. 처음 쓸 때 모모콜 앱 QR 승인이나 Google 로그인으로 연결하고, 허용할 항목을 직접 고릅니다. 전사 읽기, 문자 읽기, 문자 보내기는 기본으로 꺼져 있습니다.
- 스킬 4개: `follow-up-review`(놓친 약속 찾기), `customer-briefing`(고객 통화 준비), `crm-integration-builder`(CRM 연동 구축), `outreach-message`(다시 연락할 사람 추려 문자 보내기)

## 데이터가 가는 곳

- 이 플러그인은 모모콜 서버(`mcp.momocall.kr`)에서만 데이터를 읽어옵니다. 플러그인 자체는 다른 곳으로 데이터를 보내지 않습니다.
- 읽어온 통화 내용은 사용 중인 AI 서비스로 전달되어 해당 서비스의 정책에 따라 처리됩니다.
- 문자 보내기를 허용하면 AI가 내 휴대폰에서 내 번호로 문자를 보낼 수 있습니다. 보내기 전에 받는 사람과 내용을 확인받습니다. 문자 요금은 통신 요금제를 따릅니다.

## 비용

AI 검색(`search_conversations`)만 모모콜 AI 검색 크레딧을 1개씩 씁니다(앱과 공유). 나머지 조회는 크레딧을 쓰지 않습니다.

## 개인정보

[모모콜 개인정보처리방침](https://momocall.kr/policies/privacy)

## 문의

https://momocall.kr · cs@sellking.kr

## 표준 패키지

이 폴더의 `plugin.json`·`mcp.json`은 Plugin Creator용 Agent Plugins 1.0 매니페스트입니다. Claude Code는 기존 `.claude-plugin/plugin.json`·`.mcp.json`을 사용합니다. 이름·버전·서버 주소는 양쪽에서 동일하게 유지합니다. 소스 형식 검증과 실제 호스트 설치·로그인 검증은 별개입니다.
