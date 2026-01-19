# Antigravity Prompt Pack (TDD + CI 전제)

## 1) 테스트 생성 프롬프트
아래 요구로 tests/test_predict.py를 만들어줘:
- 엔드포인트: POST /api/v1/predict
- 정상: features 128개, batch_size=1 → 200
- 응답 키: request_id, haptic_vector(길이 64), latency_ms, model_version
- 에러: features 길이 != 128 → 422 또는 400
- 에러: batch_size=0 또는 100 → 422
- pytest 스타일, 각 테스트는 단일 책임, docstring 포함
- conftest.py의 client fixture 사용

## 2) 구현 프롬프트(/predict)
다음 테스트를 통과시키기 위해 app/routers/predict.py의 predict 본문을 구현해줘:
- app.state.onnx_session 사용
- np.float32, shape=(1,128)
- session.run(None, {"audio_features": input_array})
- output[0][0]을 list로 변환
- latency_ms 측정
- PredictLog에 성공/실패 저장
- ValueError는 400, 기타는 500

## 3) 문서 프롬프트(api_spec)
POST /api/v1/predict에 대해 docs/api_spec.md 섹션을 작성해줘:
- 목적/요청/응답/에러/예시 JSON 포함
- 제약: features=128, batch_size=1~32

## 4) 리팩토링 프롬프트
아래 코드를 더 읽기 좋게 리팩토링해줘:
- 타입 힌트, 에러 처리, 로깅 개선
- 동작 변경 금지
(코드 블록 붙여넣기)
