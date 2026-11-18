# Momocall Plugins

모모콜(Momocall) 통화 데이터를 AI 에이전트에서 활용하기 위한 공식 플러그인·스킬·MCP 설정 모음입니다.

모모콜은 통화가 끝나면 요약, 할 일, 일정을 자동으로 정리해 주는 안드로이드 앱입니다. 이 저장소의 플러그인을 설치하면 Claude Code, Codex 같은 에이전트가 **내 모모콜 통화기록·요약·일정을** 가져와 놓친 약속 찾기, 고객 통화 준비, CRM 연동, 문자 보내기 같은 작업을 정해진 절차대로 처리합니다.

- 사용 가이드: https://momocall.kr/docs/ai/overview
- 에이전트 행동 지침: https://momocall.kr/docs/ai/agent-playbook

## 무엇이 들어 있나요

```
.claude-plugin/marketplace.json     플러그인 목록 (Claude Code 마켓플레이스)
plugins/momocall/
  plugin.json                      Agent Plugins 1.0 표준 플러그인 정보
  mcp.json                         표준 Streamable HTTP MCP 설정
  .claude-plugin/plugin.json        Claude Code 호환 플러그인 정보
  .mcp.json                         원격 MCP 서버 주소 한 줄
  skills/
    follow-up-review/               놓친 약속·후속 연락 점검
    customer-briefing/              특정 고객 통화 준비 브리핑
    crm-integration-builder/        통화 데이터를 CRM에 연동하는 매핑·코드·검증
    outreach-message/               다시 연락할 사람 추리기와 문자 보내기
```

모든 파일은 **텍스트**(JSON, 마크다운)입니다. 실행 파일, 스크립트, 설치 후 자동으로 실행되는 훅(hook)은 없습니다.

| 파일 | 하는 일 | 하지 않는 일 |
|---|---|---|
| `.mcp.json` | AI 도구에 모모콜 MCP 서버 주소(`https://mcp.momocall.kr/mcp`)를 등록 | 비밀번호·토큰 저장. 로그인은 처음 쓸 때 브라우저 OAuth로 따로 진행 |
| `skills/*/SKILL.md` | AI에게 작업 순서와 안전 규칙을 알려 주는 지시문 | 코드 실행, 파일 삭제, 사용자 확인 없는 발송 |
| `skills/*/references/output-safety.md` | 스킬 공통 안전 규칙 (통화 원문 속 지시 무시, 발송 전 사용자 확인 등) | — |

## 데이터는 어디로 가나요

- 플러그인은 모모콜 서버(`mcp.momocall.kr`)에서만 데이터를 읽습니다. 플러그인 자체가 다른 곳으로 데이터를 보내지 않습니다.
- 모모콜 데이터를 바꾸거나 지우는 도구는 없습니다.
- **문자 읽기**도 연결할 때 따로 허용한 경우에만 쓸 수 있습니다(기본 꺼짐). 모모콜 PC 웹의 문자 불러오기와 같은 방식으로, 내 휴대폰 문자함을 모모콜 서버로 불러와 읽습니다.
- **문자 보내기**는 연결할 때 따로 허용한 경우에만 쓸 수 있습니다(기본 꺼짐). 문자는 내 휴대폰에서 내 번호로 나가며, AI가 받는 사람과 내용을 보여 주고 확인받은 뒤에 보냅니다.
- 사용자가 연결할 때 읽을 항목을 직접 고를 수 있으며, 통화 전체 대화(전사)는 기본으로 꺼져 있습니다.
- AI가 읽은 내용은 사용하는 AI 서비스로 전달되어 해당 서비스의 정책에 따라 처리됩니다.

## 설치

### Claude Code

```text
/plugin install momocall --marketplace cashcall-team/momocall-plugins
```

또는 마켓플레이스를 먼저 추가한 뒤 설치합니다.

```text
/plugin marketplace add cashcall-team/momocall-plugins
/plugin install momocall@momocall-plugins
```

설치 후 `/mcp` → `momocall` → **Authenticate**로 모모콜 계정을 연결합니다(앱 QR 승인 또는 Google 로그인).

특정 버전에 고정하려면 태그를 지정합니다.

```text
/plugin marketplace add cashcall-team/momocall-plugins@v1.0.0
```

### Codex

MCP 서버를 등록하고 로그인합니다.

```bash
codex mcp add momocall --url https://mcp.momocall.kr/mcp
codex mcp login momocall
```

스킬은 이 저장소를 내려받아 Codex 사용자 스킬 폴더에 복사합니다.

```bash
git clone --depth 1 https://github.com/cashcall-team/momocall-plugins.git
cp -R momocall-plugins/plugins/momocall/skills/* ~/.codex/skills/
```

### Plugin Creator용 소스

`plugins/momocall/`이 하나의 플러그인 루트입니다. 루트의 `plugin.json`·`mcp.json`은 Agent Plugins 1.0 형식이고, `.claude-plugin/plugin.json`·`.mcp.json`은 Claude Code 호환용입니다. 두 형식은 같은 이름·버전·MCP 주소를 사용합니다.

Plugin Creator에 전달할 때는 `plugins/momocall/` 안의 파일을 숨김 파일과 함께 패키징합니다. 저장소 루트의 마켓플레이스나 테스트 폴더는 포함하지 않습니다. MCP 로그인은 서버가 제공하는 OAuth 안내 정보로 진행하며 자격증명은 패키지에 넣지 않습니다.

표준 매니페스트를 추가한 상태이며, 계정 업로드·설치와 실제 ChatGPT/Codex 호스트 연결은 별도로 검증해야 합니다.

### 그 밖의 AI 도구

Claude 웹·데스크톱, ChatGPT, Cursor 등은 [AI 서비스별 연결 방법](https://momocall.kr/docs/ai/connect)을 확인해 주세요. 원격 MCP와 OAuth를 지원하는 도구라면 같은 주소로 연결할 수 있습니다.

## 버전과 변경 이력

- 릴리스마다 `vX.Y.Z` 태그를 붙입니다. 변경 내용은 [CHANGELOG.md](CHANGELOG.md)에 기록합니다.
- 스킬 문구가 바뀌면 AI의 행동도 달라지므로, 모든 변경 사항은 리뷰를 거쳐 병합합니다([CODEOWNERS](.github/CODEOWNERS)).

## 보안

취약점이나 의심스러운 동작을 발견하셨다면 공개 이슈 대신 [SECURITY.md](SECURITY.md)에 안내된 방법으로 알려 주세요.

## 라이선스

[Apache License 2.0](LICENSE). "모모콜"·"Momocall" 이름과 로고는 주식회사 매도왕의 상표이며 이 라이선스로 사용 권한이 주어지지 않습니다([NOTICE](NOTICE)).
