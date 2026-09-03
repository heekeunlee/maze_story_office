# GEMINI.md - 미로공방 (Maze Story Office)

> Antigravity AI 소설 창작 시스템: 미로/미스터리/스릴러 공방 규칙

이 저장소는 **Antigravity CLI(`agy`)**를 통해 8인의 전문 서브에이전트를 유기적으로 지휘하여 고품질 미로·미스터리 소설을 창작하는 작업 공간입니다.

## 에이전트 지침 및 페어플레이 원칙

1. **지적 유희와 개연성의 조화**:
   - 미로는 단순히 복잡한 통로가 아니라, 인간의 비밀과 트라우마가 공간화된 장치여야 합니다.
   - 단서와 복선은 독자에게 사전에 투명하게 제시되어야 합니다 (녹스 10계 및 반 다인의 법칙 현대적 계승).
2. **8단계 파이프라인 준수**:
   - `agents/01_clue_collector.md` ~ `agents/08_chief_editor.md`를 순서대로 호출하며 각 단계의 산출물을 `works/<작품폴더>/`에 기록합니다.
   - 07단계 논리 감정관의 품질 평가(100점 만점)에서 **80점 이상**을 획득하고 치명 결함이 0건일 때만 08단계 출간을 승인합니다.
3. **산출물 명명 규칙**:
   - `01_clue_research.md`: 단서 및 배경 조사
   - `02_maze_architecture.md`: 미궁 구조도 및 규칙
   - `03_character_profiles.md`: 인물 심리 및 알리바이
   - `04_plot_clue_matrix.md`: 복선/오도/반전 매트릭스
   - `05_draft.md`: 본문 초고 (6,000자 이상)
   - `06_pacing_edited.md`: 서스펜스 조율본
   - `07_critique_evaluation.md`: 논리/페어플레이 심사서
   - `08_final_novel.md`: 최종 출간작
   - `manifest.json`: 작품 메타데이터
4. **안티그래비티 CLI 권장 실행**:
   - `agy` 환경에서 작업 시 progressive disclosure 원칙에 따라 필요한 단계의 스킬과 룰만 능동적으로 참조하여 고품질의 서사를 유지합니다.
