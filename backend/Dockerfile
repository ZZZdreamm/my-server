FROM python:3.12-slim

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN poetry config virtualenvs.create false && poetry install --no-root

COPY . /app

# The --reload flag is the key here
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]