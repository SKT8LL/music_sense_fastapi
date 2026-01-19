# 김상엽 Quick Reference (역할/규칙 1장)

## 목표
- 팀원이 각자 branch에서 “구현만” 하도록, 메인 보일러플레이트와 규칙을 제공한다.
- TDD + CI를 강제한다(테스트 없으면 병합 불가).

## 김상엽 책임 범위
- 프로젝트 구조/설정(settings, logger), ORM/DB 세션, 기본 라우터(health/meta/predict 틀) 제공
- requirements.txt 중앙 관리(패키지 추가 승인)
- PR 리뷰 및 병합(테스트/CI 통과 확인)

## 브랜치 전략
- main: 보호 브랜치(직접 push 금지)
- feature/qa-and-tests: 정필상(테스트/명세)
- feature/predict-onnx: 김진욱(ONNX 추론 구현)

## TDD 규칙(강제)
- 새 기능/변경은 tests/에 테스트 코드 먼저 추가
- pytest로 “실패(RED)” 확인 후 구현
- 구현 후 pytest “성공(GREEN)” + CI 통과 시에만 병합

## 패키지 규칙(중요)
- 정필상/김진욱은 requirements.txt 임의 수정 금지
- 패키지 추가가 필요하면 “패키지명 + 이유 + 대안”을 김상엽에게 요청
- 승인 후에만 requirements.txt 반영

## PR 병합 기준(체크리스트)
- [ ] 로컬 pytest 통과
- [ ] CI(pytest) 통과
- [ ] 테스트가 변경사항을 커버
- [ ] API 스키마(Pydantic) 일관성
- [ ] 에러 처리(400/422/500) 적절
- [ ] README/문서 업데이트 필요 시 포함
