================================================================================
FLO SENSE FastAPI + ONNX 문서 패키지 요약
================================================================================

목표: TDD(테스트 우선) + CI(자동 테스트) 전제로 FastAPI 서빙 레이어 초안 문서 세트 제공

핵심 원칙:
1) 테스트를 먼저 만든다 (tests/ 먼저)
2) PR을 열면 CI에서 pytest가 자동 실행된다
3) CI가 실패하면 main 병합 금지
4) 패키지(requirements)는 김상엽이 중앙 관리

문서 구성(추천 읽기 순서):
1. 00_START_HERE.md
2. quick_ref.md
3. tdd_ci_quick_guide.md
4. implementation_roadmap.md
5. tools_rules.md
6. boilerplate_spec.md
7. readme_for_yeop.md
8. antigravity_prompt_complete.md
9. delivery_checklist.md

운영 규칙(요약):
- 정필상: tests/ 우선 작성 + api_spec 문서화
- 김진욱: tests를 통과시키는 구현(/predict ONNX 연결)
- 김상엽: 보일러플레이트/ORM/패키지 관리 + 리뷰/병합
================================================================================
