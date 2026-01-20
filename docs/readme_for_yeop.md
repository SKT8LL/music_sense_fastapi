# 김상엽 운영 가이드(리더용)

## 리더 목표
- 팀이 TDD/CI 규칙을 지키면서도 속도를 잃지 않게 한다.
- main 브랜치 안정성을 보장한다.

## 오늘 할 일(체크리스트)
- [ ] 문서 세트 GitHub 커밋
- [ ] 팀 슬랙 공지(필독: Quick Reference + TDD/CI Guide)
- [ ] 온보딩 30분 일정 확정
- [ ] 보일러플레이트 PR(#0) 준비

## 온보딩 30분 구성
- 10분: 프로젝트 구조 설명(어디에 무엇을 작성하는가)
- 10분: TDD 흐름(테스트 먼저 → 구현 → CI)
- 10분: 브랜치/PR 규칙(패키지 승인 포함)

## 리뷰 원칙
- 테스트 없는 PR 병합 금지
- CI 실패 PR 병합 금지
- 도구가 만든 코드라도 스타일/예외/스키마 일관성 확인

## 리스크 대응
- 모델 스키마 불일치: meta 문서/스키마부터 확정
- 레이턴시 초과: 먼저 정확성/테스트 통과, 이후 최적화
- 패키지 충돌: 중앙 관리로 차단

## 현재 보일러플레이트 상태
- main.py: /api/v1 health/meta/predict 라우터 include 완료, lifespan에서 DB 테이블 생성 + onnx_session placeholder 바인딩
- app/routers: health/meta/predict 스키마 고정, predict는 더미 추론 반환(진욱 교체 예정)
- app/schemas: Health/Meta/Predict 요청/응답 스키마 명시(128→64 float, batch_size 1~32)
- settings.py: DATABASE_URL, MODEL_PATH, MODEL_VERSION, LOG_LEVEL, ENV 환경변수 지원
- logger.py: get_logger 헬퍼로 콘솔 로깅 구성
