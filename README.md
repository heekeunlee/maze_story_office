# 🗝️ 미로공방 (Maze Story Office)

> **"출구를 찾는 자에게만 드러나는 진실, 미로처럼 얽힌 복선과 심리의 궤적을 짓는 곳."**

[![Antigravity CLI](https://img.shields.io/badge/Orchestrator-Antigravity%20CLI%20(agy)-0284c7?style=flat-square&logo=google)](https://antigravity.google)
[![GitHub Pages](https://img.shields.io/badge/Web%20Office-Live%20Demo-38bdf8?style=flat-square&logo=github)](https://heekeunlee.github.io/maze_story_office/)
[![Quality Gate](https://img.shields.io/badge/Quality%20Gate-100%20Rubric%20(PASS%20%E2%89%A5%2080)-10b981?style=flat-square)](docs/QUALITY.md)

미로공방은 **Google Antigravity CLI(`agy`)**와 8인의 전문 서브에이전트가 단서 수집, 미궁 설계, 인물 심리, 복선·트릭 매트릭스, 집필, 서스펜스 조율, 논리 감정, 출간 승인을 체계적으로 분담하여 지적 쾌감과 극한의 서스펜스를 선사하는 미로·미스터리·스릴러 소설 제작소입니다.

🌐 **미로공방 인터랙티브 웹 오피스**: [https://heekeunlee.github.io/maze_story_office/](https://heekeunlee.github.io/maze_story_office/)

---

## 🏛️ 3대 자매 공방 네트워크 (Sister Story Studios)

| 공방 이름 | 기반 AI 플랫폼 | 장르 및 목표 | 저장소 |
|---|---|---|---|
| **동화공방 (Fairy Tale Office)** | **Claude Code** | 촛불 켜진 목재 공방, 8인의 주옥같은 창작동화 제작 | [fairy_tale_office](https://github.com/heekeunlee/fairy_tale_office) |
| **여운공방 (Touching Story Office)** | **OpenAI Codex** | 마지막 문장을 덮은 뒤에도 오래 머무는 감동과 존엄의 소설 | [touching_story_office](https://github.com/heekeunlee/touching_story_office) |
| **미로공방 (Maze Story Office)** | **Antigravity CLI** | 복선과 트릭을 직조하는 정통 미로·미스터리·서스펜스 소설 | [maze_story_office](https://github.com/heekeunlee/maze_story_office) |

---

## 👥 8인 제작진 (The 8 Labyrinth Agents)

| 번호 | 이름 | 직책 | 상징 도구 | 핵심 역할 및 산출물 | 명세서 |
|:---:|---|---|---|---|---|
| **01** | **강도윤** | **단서채집가** | 🔍 돋보기와 단서 핀보드 | 사건 발단, 공간/기믹 설정, 사실/과학 조사 (`01_clue_research.md`) | [spec](agents/01_clue_collector.md) |
| **02** | **백시우** | **미궁설계자** | 📐 황동 컴퍼스와 청사진 | 4계층 미로 구조도(분기/막다른 길/출구 법칙) (`02_maze_architecture.md`) | [spec](agents/02_labyrinth_architect.md) |
| **03** | **송채은** | **인물심리가** | ⏳ 모래시계와 심리 가면 | 탐색자/용의자 결핍, 알리바이, 불신망 (`03_character_profiles.md`) | [spec](agents/03_character_psychologist.md) |
| **04** | **민태오** | **복선·트릭엔지니어** | ⚙️ 정밀 톱니와 열쇠 | 복선-오도 전수 매트릭스, 2단 반전 설계 (`04_plot_clue_matrix.md`) | [spec](agents/04_trick_engineer.md) |
| **05** | **서연우** | **미스터리 소설가** | ✒️ 흑요석 만년필 | 오감 묘사, 폐쇄 공간의 긴장감, 초고 집필 (`05_draft.md`) | [spec](agents/05_mystery_novelist.md) |
| **06** | **안하린** | **서스펜스 조율사** | ✂️ 은빛 가위와 메트로놈 | 텐션 완급 조절, 단서 명도 교정, 대화 정련 (`06_pacing_edited.md`) | [spec](agents/06_suspense_editor.md) |
| **07** | **고진혁** | **논리·미궁 감정관** | ⚖️ 청동 천칭과 진실 촛대 | 페어플레이 검증, 타임라인/결함 전수 심사 (`07_critique_evaluation.md`) | [spec](agents/07_logic_examiner.md) |
| **08** | **반채현** | **미로 총괄편집장** | 🗝️ 황금 열쇠와 실링 인장 | Antigravity CLI 오케스트레이션, 최종 출간 (`08_final_novel.md`) | [spec](agents/08_chief_editor.md) |

---

## 🔄 제작 워크플로 (Workflow Pipeline)

```text
[사용자 기획 브리프]
         │
         ▼
┌─────────────────────────────────┐
│  Phase 1. 단서 및 배경 수집     │ ──▶ 01. 단서채집가 (강도윤)
└─────────────────────────────────┘      산출물: 01_clue_research.md
         │
         ▼
┌─────────────────────────────────┐
│  Phase 2. 구조 및 인물 설계     │ ──▶ 02. 미궁설계자 (백시우) & 03. 인물심리가 (송채은)
└─────────────────────────────────┘      산출물: 02_maze_architecture.md, 03_character_profiles.md
         │
         ├───▶ [Gate 1. 아키텍처 게이트: 공간-동기 정합성 점검]
         ▼
┌─────────────────────────────────┐
│  Phase 3. 복선·트릭 매트릭스    │ ──▶ 04. 복선·트릭엔지니어 (민태오)
└─────────────────────────────────┘      산출물: 04_plot_clue_matrix.md
         │
         ├───▶ [Gate 2. 트릭 게이트: 페어플레이 및 2단 반전 무결성 점검]
         ▼
┌─────────────────────────────────┐
│  Phase 4. 집필 및 서스펜스 조율 │ ──▶ 05. 미스터리소설가 (서연우) & 06. 서스펜스조율사 (안하린)
└─────────────────────────────────┘      산출물: 05_draft.md, 06_pacing_edited.md
         │
         ▼
┌─────────────────────────────────┐
│  Phase 5. 논리 및 결함 감정     │ ──▶ 07. 논리·미궁감정관 (고진혁)
└─────────────────────────────────┘      산출물: 07_critique_evaluation.md
         │
         ├───▶ [Gate 3. 최종 출간 게이트: 80점 이상 & 결함 0건 필수]
         │         ├─ PASS ──┐
         │         └─ FAIL ──┴──▶ Phase 4 (집필) 또는 Phase 3 (트릭)으로 피드백 환류
         ▼
┌─────────────────────────────────┐
│  Phase 6. 최종 출간 및 아카이빙 │ ──▶ 08. 미로총괄편집장 (반채현)
└─────────────────────────────────┘      산출물: 08_final_novel.md, manifest.json
```

자세한 제작 지침은 [작품 제작 워크플로](docs/WORKFLOW.md)와 [품질 루브릭](docs/QUALITY.md)을 참조하세요.

---

## 💻 Antigravity CLI(`agy`)에서 사용하기

터미널에서 `agy` 명령어로 8인의 서브에이전트를 호출하여 완결된 단편 소설을 즉시 생성할 수 있습니다:

```bash
# Antigravity CLI 단일 마스터 프롬프트 실행
agy "AGENTS.md와 agents/의 8인 역할을 순차 가동하여, 
자정에만 열리는 고문서 도서관의 뫼비우스 서가에 갇힌 암호해독가의 탈출기를 작성해줘. 
단서가 논리적으로 회수되는 정통 미스터리 스릴러(분량 6,000자 이상)로 완성할 것."
```

세부적인 Antigravity CLI 활용법은 [Antigravity 활용 가이드](docs/ANTIGRAVITY_GUIDE.md)에 안내되어 있습니다.

---

## 📂 저장소 구조 (Repository Layout)

```text
├── .agents/
│   ├── rules/                 # Antigravity 점진적 룰 (페어플레이, 미궁 논리)
│   └── skills/                # Antigravity 전용 스킬 (maze-story-craft)
├── agents/                    # 8인의 전문 서브에이전트 역할 지침서
├── docs/                      # 워크플로, 품질 루브릭, Antigravity 가이드
├── works/                     # 작품별 8단계 중간 산출물 및 최종 출간 원고
│   └── 01_shadow_of_the_clockwork_maze/
├── site/                      # GitHub Pages 인터랙티브 웹 오피스 및 뷰어
├── scripts/                   # 저장소 무결성 및 품질 검증 도구
├── .github/workflows/         # GitHub Pages 자동 배포 액션
├── AGENTS.md                  # 미로공방 운영 헌장 (Orchestrator Guide)
├── GEMINI.md                  # Antigravity 지침 및 룰
└── README.md
```

---

## 🛠️ 검증 및 로컬 서버 실행

```bash
# 1. 저장소 무결성 및 8인 산출물 검증
python3 scripts/validate.py

# 2. 로컬 웹 오피스 실행
python3 -m http.server 8000 --directory site
```

`main` 브랜치에 변경 사항이 푸시되면 GitHub Actions가 `site/` 디렉토리를 GitHub Pages로 자동 배포합니다.
*(저장소 Settings → Pages → Source가 **GitHub Actions**로 설정되어 있어야 합니다.)*