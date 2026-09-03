#!/usr/bin/env python3
"""
미로공방 (Maze Story Office) 무결성 및 품질 검증 스크립트
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

errors = []

# 1. 필수 기본 파일 검증
required_core = [
    "AGENTS.md",
    "GEMINI.md",
    "README.md",
    "docs/WORKFLOW.md",
    "docs/QUALITY.md",
    "docs/ANTIGRAVITY_GUIDE.md",
    "docs/PERSONNEL_RECORDS.md",
    ".agents/rules/fair-play-rule.md",
    ".agents/rules/maze-logic-rule.md",
    ".agents/skills/maze-story-craft/SKILL.md",
    "site/index.html",
    "site/.nojekyll",
    ".github/workflows/pages.yml",
]

# 1-1. 에이전트 프로필 이미지 검증
agent_photos = [
    "01_doyoon_kang.jpg",
    "02_siwoo_baek.jpg",
    "03_chaeeun_song.jpg",
    "04_taeo_min.jpg",
    "05_yeonwoo_seo.jpg",
    "06_harin_ahn.jpg",
    "07_jinhyuk_ko.jpg",
    "08_chaehyun_ban.jpg",
]

for photo in agent_photos:
    target = ROOT / "site" / "assets" / "agents" / photo
    if not target.exists():
        errors.append(f"[ERROR] 에이전트 사진 누락: site/assets/agents/{photo}")


for file_path in required_core:
    target = ROOT / file_path
    if not target.exists():
        errors.append(f"[ERROR] 필수 파일 누락: {file_path}")

# 2. 8인 서브에이전트 명세서 검증
required_agents = [
    "01_clue_collector.md",
    "02_labyrinth_architect.md",
    "03_character_psychologist.md",
    "04_trick_engineer.md",
    "05_mystery_novelist.md",
    "06_suspense_editor.md",
    "07_logic_examiner.md",
    "08_chief_editor.md",
]

for agent in required_agents:
    target = ROOT / "agents" / agent
    if not target.exists():
        errors.append(f"[ERROR] 에이전트 명세서 누락: agents/{agent}")

# 3. 작품 디렉토리 및 산출물 검증
works_dir = ROOT / "works"
if not works_dir.exists():
    errors.append("[ERROR] works 디렉토리가 존재하지 않습니다.")
else:
    works = list(works_dir.glob("*"))
    if not works:
        errors.append("[ERROR] 등록된 작품이 없습니다.")
    for work in works:
        if not work.is_dir():
            continue
        manifest_file = work / "manifest.json"
        if not manifest_file.exists():
            errors.append(f"[ERROR] 작품 매니페스트 누락: {work.name}/manifest.json")
            continue
        try:
            with open(manifest_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            required_keys = ["id", "title", "rubric_score", "verdict", "word_count"]
            for k in required_keys:
                if k not in data:
                    errors.append(f"[ERROR] {manifest_file.name} 필수 키 누락: {k}")
            if data.get("rubric_score", 0) < 80 and data.get("verdict") == "PASS":
                errors.append(f"[ERROR] 점수 미달(80점 미만)인데 PASS 처리됨: {work.name}")
        except Exception as e:
            errors.append(f"[ERROR] manifest.json 파싱 실패: {manifest_file} ({e})")

        # 필수 산출물 단계 검증
        expected_steps = [
            "01_clue_research.md",
            "02_maze_architecture.md",
            "03_character_profiles.md",
            "04_plot_clue_matrix.md",
            "05_draft.md",
            "06_pacing_edited.md",
            "07_critique_evaluation.md",
            "08_final_novel.md",
        ]
        for step in expected_steps:
            if not (work / step).exists():
                errors.append(f"[ERROR] 작품 단계 산출물 누락: {work.name}/{step}")

# 4. 결과 보고
print("=" * 60)
print(" 🏰 미로공방 (Maze Story Office) 시스템 무결성 검증 결과")
print("=" * 60)

if errors:
    print(f"❌ 총 {len(errors)}개의 결함이 발견되었습니다:")
    for err in errors:
        print(f"  {err}")
    sys.exit(1)
else:
    print("✅ 모든 에이전트 명세, 규칙, 스킬, 워크플로 및 작품 산출물이 완벽합니다!")
    print("✨ 품질 기준: 100점 만점 / PASS 기준(80점) 충족")
    print("=" * 60)
    sys.exit(0)
