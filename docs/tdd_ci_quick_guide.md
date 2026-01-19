# TDD + CI Quick Guide (5분)

## 왜 TDD + CI인가
- CI에서 pytest가 자동으로 돌기 때문에, 테스트가 곧 “병합 게이트”가 된다.
- 테스트 없이 구현만 하면 장기적으로 유지보수/협업 비용이 폭증한다.

## 기본 흐름(반드시)
1) tests/에 테스트 먼저 작성
2) pytest 실행 → 실패(RED) 확인
3) 구현 코드 작성
4) pytest 재실행 → 성공(GREEN) 확인
5) PR 오픈 → CI 통과 확인 → 리뷰 후 병합

## /predict 예시
- 정필상: tests/test_predict.py 작성
  - 정상: features 128개 → 200 + haptic_vector 64개
  - 에러: features 길이 오류 → 422 또는 400
  - 에러: batch_size 범위 오류 → 422
- 김진욱: 위 테스트를 통과시키는 구현을 app/routers/predict.py에 추가

## CI 규칙
- PR이 열리면 CI가 pytest 실행
- CI 실패(PR 빨간 X) 상태면 병합 금지
- 수정 push 시 CI 자동 재실행

## 역할별 체크
- 정필상(테스트): “정상/에러/경계” 최소 1개씩 포함
- 김진욱(구현): 테스트가 기대하는 응답 스키마/에러코드 충족
- 김상엽(리뷰): CI green + 테스트 커버 확인 후 병합
