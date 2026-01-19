---
description: FLO SENSE Project Rules (TDD, CI, Architecture)
globs: "**/*"
always_on: true
---
# FLO SENSE Project Rules

You are working on the FLO SENSE project (FastAPI + ONNX). You MUST follow these rules.

## 1. Architecture Constraints
- **Framework**: FastAPI (Python 3.10+), SQLAlchemy, ONNX Runtime.
- **Directory Structure**:
    - `app/routers/`: API endpoints.
    - `app/models.py`: SQLAlchemy ORM.
    - `app/schemas.py`: Pydantic Models.
    - `app/database.py`: DB Session (`get_db` dependency).
    - `tests/`: Pytest tests.
- **Dependency Injection**: Always use `Depends(get_db)` for DB sessions.

## 2. TDD (Test Driven Development) Principle
**Strictly follow "Red -> Green -> Refactor"**:
1.  **Tests First**: BEFORE implementing any functional code, write the test in `tests/test_xxx.py`.
2.  **Verify Failure**: Run the test to confirm it fails (or errors) because the feature is missing.
3.  **Implement**: Write the minimal implementations in `app/`.
4.  **Verify Success**: Run the test again to pass.

## 3. CI/CD Safety
- `pytest` runs in CI. **Never commit code that breaks tests.**
- Do not introduce "sleep" or flaky tests.
- Use `uv` for package management (`uv pip install ...`).

## 4. Response Style
- Provide code snippets in small chunks.
- When creating a new file, provide the FULL content.
- Be concise.
