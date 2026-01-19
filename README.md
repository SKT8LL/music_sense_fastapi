# FLO SENSE (FastAPI + ONNX)

FLO SENSE의 Music-to-Haptic 변환을 위한 API 서버 프로젝트입니다.
FastAPI와 ONNX Runtime을 사용하여 오디오 신호를 햅틱 패턴으로 추론합니다.

## 1. Getting Started

### Prerequisites
- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (Package Manager)

### Installation
```bash
# 1. Clone & Enter
git clone <repo-url>
cd music_sense_fastapi

# 2. Setup Venv & Install Dependencies (using uv)
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### Configuration
`settings.py`는 환경 변수를 통해 설정됩니다.
`.env.example`을 복사하여 `.env`를 만드세요.
```bash
cp .env.example .env
```

### Running Server
```bash
# Development Mode
uvicorn main:app --reload

# Swagger UI
http://localhost:8000/docs
```

---

## 2. Team Roles & Responsibilities

이 프로젝트는 **TDD(Test Driven Development)** 원칙을 엄격하게 따릅니다.

### 🧑‍💻 상엽 (Architect / Lead)
- **책임**: 프로젝트 구조, 공통 모듈(`database`, `settings`), CI/CD 파이프라인.
- **Next Tasks**:
    - `meta` 엔드포인트 구현 (TDD)
    - Azure 배포 파이프라인 구성

### 🧑‍💻 필상 (Test / QA / Docs)
- **책임**: **Test Code 작성 (TDD Start)**, API 명세서(`docs/api_spec.md`), QA.
- **Next Tasks**:
    - `tests/test_predict.py` 작성 (정상/에러 케이스 포함)
    - `docs/api_spec.md` 작성

### 🧑‍💻 진욱 (AI Logic / Implementation)
- **책임**: `/predict` 엔드포인트, ONNX 모델 로딩 및 추론 로직 연결.
- **Next Tasks**:
    - (필상이 만든) `tests/test_predict.py` 실행 및 실패 확인
    - `app/routers/predict.py` 구현 (ONNX 런타임 연동) 및 테스트 통과

---

## 3. How to Work (TDD Workflow)

우리는 **AntiGravity(LLM Tool)**의 도움을 받아 개발하지만, 주도권은 개발자에게 있습니다.

### Step 1: 테스트 작성 (Red)
새 기능을 만들 때 가장 먼저 테스트 코드를 작성합니다.
> "`/predict` API가 잘못된 오디오 데이터를 받으면 400 에러를 뱉는지 테스트해줘."

```bash
# 실행 및 실패 확인
uv run pytest tests/test_feature.py
```

### Step 2: 구현 (Green)
테스트를 통과하기 위한 최소한의 코드를 작성합니다.
> "ONNX 런타임을 로드해서 inference를 돌리는 코드를 `app/routers/predict.py`에 짜줘."

### Step 3: 실행 및 검증 (Refactor)
```bash
uv run pytest
```
모든 테스트가 통과(Green)해야 커밋할 수 있습니다.

---

## 4. Antigravity/LLM Usage
- `.agent/rules/project_rules.md`에 프로젝트 규칙이 정의되어 있습니다.
- 새로운 기능을 만들 때 `/tdd` 워크플로우를 참고하세요.
