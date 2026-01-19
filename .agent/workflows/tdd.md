---
description: Implement a new feature using TDD
---
I will guide you through implementing a new feature using TDD.

1.  **Ask for Feature Details**:
    -   What is the feature? (e.g. "POST /predict")
    -   What are the success/error scenarios?

2.  **Create Test (Red)**:
    -   Create/Update `tests/test_<feature>.py`.
    -   Write proper `pytest` functions.
    -   // turbo
    -   Run `uv run pytest tests/test_<feature>.py` to confirm failure.

3.  **Implement (Green)**:
    -   Create/Update `app/routers/<feature>.py` or `app/models.py`.
    -   Register router in `main.py` if new.

4.  **Verify (Refactor)**:
    -   // turbo
    -   Run `uv run pytest tests/test_<feature>.py` to confirm pass.
    -   If failed, fix implementation and repeat.
