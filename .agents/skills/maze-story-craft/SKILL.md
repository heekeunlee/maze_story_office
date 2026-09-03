---
name: maze-story-craft
description: Antigravity Skill for end-to-end creation, verification, and publication of 8-agent mystery & labyrinth stories.
---

# Maze Story Craft Skill

이 스킬은 Antigravity CLI(`agy`)에서 미로공방의 8인 서브에이전트 파이프라인을 작동하여 결함 없는 고품질 미로 소설을 완성하는 표준 실행 절차를 제공합니다.

## 실행 절차 (Execution Pipeline)

1. **Phase 1: 단서 및 배경 조사 (`01_clue_collector`)**
   - 사용자 브리프 분석
   - 5대 핵심 단서 및 미궁 배경 설계
   - 산출물: `01_clue_research.md`

2. **Phase 2: 미궁 아키텍처 및 인물 심리 설계 (`02_labyrinth_architect` & `03_character_psychologist`)**
   - 4계층 미로 구조 청사진 작성
   - 인물 3~5인의 결핍, 욕망, 알리바이 네트워크 구축
   - [게이트 1: 아키텍처 점검]
   - 산출물: `02_maze_architecture.md`, `03_character_profiles.md`

3. **Phase 3: 복선 매트릭스 및 트릭 설계 (`04_trick_engineer`)**
   - 복선(Clue) 및 오도(Red Herring) 전수 매트릭스 작성
   - 2단 반전 및 챕터별 타임라인 확정
   - [게이트 2: 트릭 무결성 점검]
   - 산출물: `04_plot_clue_matrix.md`

4. **Phase 4: 초고 집필 및 서스펜스 조율 (`05_mystery_novelist` & `06_suspense_editor`)**
   - 6,000자 이상 고밀도 서스펜스 소설 초고 집필
   - 문장 리듬, 템포, 텐션, 대화 정련
   - 산출물: `05_draft.md`, `06_pacing_edited.md`

5. **Phase 5: 논리 감정 및 품질 심사 (`07_logic_examiner`)**
   - 100점 만점 품질 루브릭 채점
   - 결함 0건 & 80점 이상 시 PASS, 미달 시 4/5단계 재작업
   - 산출물: `07_critique_evaluation.md`

6. **Phase 6: 최종 출간 및 등록 (`08_chief_editor`)**
   - 최종 윤문 및 포맷팅 (`08_final_novel.md`)
   - 메타데이터 매니페스트 작성 (`manifest.json`)
   - `site/` 오피스 뷰어와 동기화
