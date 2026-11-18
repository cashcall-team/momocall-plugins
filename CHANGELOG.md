# 변경 이력

## 미출시

- 문자 보내기: MCP 도구 `send_sms`·`get_sms_status`와 스킬 `outreach-message` 추가. 공통 안전 규칙에 문자 발송 규칙 추가
- 문자 읽기: MCP 도구 `list_sms_threads`·`get_sms_messages`·`list_phone_contacts`·`import_sms`·`get_sms_import_status` 추가. 공통 안전 규칙에 문자 읽기 규칙 추가

- Plugin Creator용 Agent Plugins 1.0 `plugin.json`·`mcp.json` 추가. 기존 Claude Code 설정 유지
- 표준·Claude 매니페스트의 메타데이터와 서버 주소 일치 검사 추가

## v1.0.0 — 2026-11-16

- 첫 공개. `momocall` 플러그인: 원격 MCP 서버 연결(`https://mcp.momocall.kr/mcp`, 읽기 전용) + 스킬 3종(`follow-up-review`, `customer-briefing`, `crm-integration-builder`)
- Apache License 2.0
