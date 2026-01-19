# Implementation Roadmap (Week 1~2)

## 목표
- Week 2까지 “ONNX 추론 FastAPI 서버”를 CI 통과 상태로 main에 병합.

## 산출물(최소)
- GET /api/v1/healthz
- GET /api/v1/meta
- POST /api/v1/predict (ONNX 연결)
- tests/: health/predict 테스트
- docs/api_spec.md
- Dockerfile + docker-compose.yml(선택이지만 권장)

## 일정(권장)
### Day 0 (김상엽)
- 보일러플레이트/ORM/기본 라우터 틀 제공
- 테스트 실행 가능한 conftest 준비

### Day 1~2 (정필상)
- tests/test_health.py, tests/test_predict.py 작성(TDD)
- docs/api_spec.md 작성

### Day 2~4 (김진욱)
- tests를 통과시키는 /predict ONNX 구현
- 입력 변환(np.float32, shape=(1,128)) 및 출력 list 변환

### Day 5 (김상엽)
- PR 리뷰(테스트/CI/코드 스타일) 후 병합

## PR 템플릿(요약)
### PR(정필상): tests + spec
- 변경: tests/*.py, docs/api_spec.md
- 조건: pytest 통과, 에러 케이스 포함

### PR(김진욱): ONNX predict
- 변경: app/routers/predict.py
- 조건: pytest 통과, 에러 처리, 성능 측정(가능하면)

## 성공 기준
- pytest 전체 통과
- CI green
- /predict가 실제 ONNX를 호출(모델 제공 시점 이후)
