"""플러그인 패키지 규칙 검사 — 표준 라이브러리만 쓴다.

실행: `python3 tests/test_plugin_package.py` 또는 `pytest tests -q`
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "momocall"
SKILL_NAMES = ["crm-integration-builder", "customer-briefing", "follow-up-review", "outreach-message"]
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg"}
SECRET_PATTERN = re.compile(r"(mmc_(at|rt)_|sk-[A-Za-z0-9]{20}|AIza[0-9A-Za-z_-]{20}|-----BEGIN)")


def test_manifest_and_marketplace() -> None:
    manifest = json.loads((PLUGIN / ".claude-plugin/plugin.json").read_text())
    assert re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", manifest["name"])
    assert not manifest["name"].startswith(("claude-", "anthropic-"))
    market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
    entry = market["plugins"][0]
    assert entry["name"] == manifest["name"]
    assert entry["source"] == "./plugins/momocall" and (ROOT / entry["source"]).is_dir()
    assert len((PLUGIN / "README.md").read_text().split()) >= 40
    assert (ROOT / "LICENSE").exists()
    assert manifest["privacyPolicyUrl"].startswith("https://")
    assert (PLUGIN / ".claude-plugin/icon.png").read_bytes().startswith(b"\x89PNG")


def test_mcp_server_points_to_production() -> None:
    servers = json.loads((PLUGIN / ".mcp.json").read_text())["mcpServers"]
    assert servers["momocall"] == {"type": "http", "url": "https://mcp.momocall.kr/mcp"}


def test_skills_follow_rules() -> None:
    skills = sorted(p for p in (PLUGIN / "skills").iterdir() if p.is_dir())
    assert [s.name for s in skills] == SKILL_NAMES
    for skill in skills:
        text = (skill / "SKILL.md").read_text()
        front = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL).group(1)
        meta = dict(line.split(": ", 1) for line in front.splitlines())
        assert meta["name"] == skill.name and len(meta["name"]) <= 64
        assert 1 <= len(meta["description"]) <= 1024 and "<" not in meta["description"]
        assert len(text.splitlines()) < 500
        assert "references/output-safety.md" in text and (skill / "references/output-safety.md").exists()


def test_no_secrets_in_package() -> None:
    for path in PLUGIN.rglob("*"):
        if path.is_file() and path.suffix not in IMAGE_SUFFIXES:
            assert not SECRET_PATTERN.search(path.read_text()), path


def test_portable_manifests_match_claude_package() -> None:
    portable = json.loads((PLUGIN / "plugin.json").read_text())
    legacy = json.loads((PLUGIN / ".claude-plugin/plugin.json").read_text())
    assert portable.pop("$schema") == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
    assert portable == legacy
    mcp = json.loads((PLUGIN / "mcp.json").read_text())
    legacy_mcp = json.loads((PLUGIN / ".mcp.json").read_text())
    assert mcp["$schema"] == "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json"
    assert set(mcp["mcpServers"]) == set(legacy_mcp["mcpServers"])
    for name, server in mcp["mcpServers"].items():
        assert server["type"] == "streamable-http"
        assert server["url"] == legacy_mcp["mcpServers"][name]["url"]
        assert set(server) == {"type", "url"}


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("PASS", name)
