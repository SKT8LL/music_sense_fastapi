# Boilerplate Spec (김상엽 제공 범위)

## 목표
정필상/김진욱이 각자 branch에서 “구현만” 할 수 있도록,
- 구조
- ORM/DB
- 설정/로깅
- 라우터 틀
- 테스트 실행 기반
을 먼저 깔아준다.

## 권장 디렉토리 구조
flo-sense-api/
- main.py
- settings.py
- logger.py
- requirements.txt
- Dockerfile
- docker-compose.yml
- app/
  - database.py
  - models.py
  - schemas.py
  - routers/
    - health.py
    - meta.py
    - predict.py  (TODO: ONNX 연결은 김진욱)
- tests/
  - conftest.py   (TestClient + test DB)
  - test_health.py (정필상)
  - test_predict.py (정필상)
- docs/
  - api_spec.md (정필상)

## 필수 엔드포인트 정의
- GET /api/v1/healthz
  - 응답: status, onnx_providers, model_loaded, database_ok, timestamp
- GET /api/v1/meta
  - 응답: model_name, version, input_shape, output_shape, dtype, latency_target_ms
- POST /api/v1/predict
  - 요청: features(128 floats), batch_size(1~32)
  - 응답: request_id, haptic_vector(64 floats), latency_ms, model_version

## ORM(최소)
- PredictLog
  - id(uuid)
  - input_features(JSON str)
  - output_haptic(JSON str)
  - latency_ms(float)
  - status(success/error)
  - error_message(optional)
  - created_at
- ModelMetadata
  - model_name, version
  - input_shape, output_shape
  - input_dtype, output_dtype
  - latency_target_ms
  - updated_at

## predict.py에 남길 TODO(명확히)
- “여기에 ONNX 추론 로직 구현” 주석 + 입력/출력 스키마 주석
- 더미 출력으로 응답 스키마를 유지(테스트 작성/Swagger 확인 용)

## 테스트 기반(김상엽)
- tests/conftest.py에서:
  - FastAPI TestClient fixture 제공
  - (가능하면) SQLite 테스트 DB override
