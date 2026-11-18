# 기여 안내

이슈와 PR을 환영합니다. 스킬 문구는 AI의 행동을 바꾸므로 아래 기준으로 리뷰합니다.

## 스킬을 고칠 때

- 모든 스킬은 `references/output-safety.md`의 공통 안전 규칙을 따라야 합니다. 이 규칙을 약화하는 변경은 받지 않습니다.
- 모모콜 데이터(통화기록·요약·할 일)는 바꿀 수 없습니다. "모모콜에 저장·수정한다"는 단계를 넣지 않습니다.
- 문자 보내기(`send_sms`)를 쓰는 단계에는 "받는 사람과 내용을 사용자에게 보여 주고 확인받는다"를 반드시 넣습니다.
- 메일·메시지 발송, 외부 URL 열기, 운영 시스템 반영은 "사용자가 직접 요청하고 확인한 경우에만" 진행하도록 둡니다.
- AI 검색(`search_conversations`)은 크레딧을 쓰므로 요청 하나에 1회를 기본으로 합니다.
- 도구 이름·필드는 [도구 레퍼런스](https://momocall.kr/docs/ai/tools)와 맞춥니다.

## 검증

PR을 올리기 전에 Claude Code로 구조를 검증합니다.

```bash
claude plugin validate .
```

패키지 형식·호환 매니페스트 일치 검사는 `python3 tests/test_plugin_package.py`로 실행합니다.

## 릴리스

1. `plugins/momocall/plugin.json`과 `plugins/momocall/.claude-plugin/plugin.json`의 `version`을 동일하게 올립니다.
2. [CHANGELOG.md](CHANGELOG.md)에 변경 내용을 적습니다.
3. 병합 후 `vX.Y.Z` 태그를 붙입니다.

## 라이선스

기여한 내용은 [Apache License 2.0](LICENSE)으로 배포됩니다.
