
export PYTHONDONTWRITEBYTECODE=1
export ENVIRONMENT=dev


python -m uvicorn src.main:app --port 8000 --reload
