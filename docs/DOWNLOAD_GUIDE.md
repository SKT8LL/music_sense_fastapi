# DOWNLOAD & SETUP GUIDE

## 1. Source Code
이 프로젝트는 Git으로 관리됩니다.

```bash
# Clone Repository
git clone <REPOSITORY_URL>
cd music_sense_fastapi

# Setup Virtual Environment (using uv)
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

## 2. Documents
`docs/` 디렉토리에 모든 프로젝트 문서가 포함되어 있습니다.
이 디렉토리만 따로 압축해서 팀원들에게 공유할 수도 있습니다.
(하지만 git repository 내에서 보는 것을 권장합니다.)

## 3. Environment Variables
`settings.py` 구동을 위해 `.env` 파일이 필요합니다.
```bash
cp .env.example .env
# .env 파일을 열어서 DB 정보 등을 수정하세요.
```
