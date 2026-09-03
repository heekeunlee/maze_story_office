# Antigravity CLI 활용 가이드 (Antigravity CLI Guide)

> 미로공방을 Antigravity CLI(`agy`)에서 최고 효율로 구동하는 방법

---

## 1. Antigravity CLI 환경 소개

미로공방은 Google Antigravity 개발 플랫폼의 CLI 인터페이스(`agy`)를 기반으로 설계되었습니다. Antigravity의 **점진적 공개(Progressive Disclosure)**, **서브에이전트 조율(Subagent Orchestration)**, **자동화 검증** 메커니즘을 적극 활용합니다.

---

## 2. 기본 실행 방법

### 단일 마스터 프롬프트로 전체 8인 파이프라인 가동
터미널에서 아래 명령어로 8인의 서브에이전트를 순차 가동하여 완결된 단편 소설을 생성할 수 있습니다.

```bash
agy "AGENTS.md와 agents/의 8인 역할을 사용해,
폭설로 고립된 산장의 지하 와인창고에서 발견된 기하학적 미로의 탈출기를 써줘.
시간제한 기믹과 2단 반전을 포함하고, 품질 루브릭 80점 이상을 달성할 것."
```

### 단계별 대화형 실행 (Interactive Stepping)
각 단계를 하나씩 점검하며 정밀하게 진행하고 싶을 때:

```bash
# 1단계: 단서 및 배경 조사
agy "agents/01_clue_collector.md의 강도윤 역할로, '크로노스 하우스'의 시계태엽 미로 배경과 단서 5종을 조사해줘."

# 2단계: 미궁 및 인물 설계
agy "agents/02_labyrinth_architect.md와 agents/03_character_psychologist.md를 가동하여 청사진과 인물 심리망을 작성해줘."

# 3단계: 복선 및 트릭 매트릭스
agy "agents/04_trick_engineer.md를 호출하여 복선/오도 매트릭스를 구성해줘."

# 4단계: 본문 집필 및 조율
agy "agents/05_mystery_novelist.md와 agents/06_suspense_editor.md로 6,000자 이상 본문을 집필하고 다듬어줘."

# 5단계 & 6단계: 논리 감정 및 출간
agy "agents/07_logic_examiner.md로 채점하고, PASS 시 agents/08_chief_editor.md로 최종 출간작과 manifest.json을 생성해줘."
```

---

## 3. 검증 및 로컬 서버 실행

```bash
# 1. 저장소 구조 및 산출물 유효성 검증
python3 scripts/validate.py

# 2. 로컬에서 인터랙티브 웹 오피스 확인
python3 -m http.server 8000 --directory site
```
