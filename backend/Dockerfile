FROM python:3.11-slim

# Install poetry
RUN pip install poetry

WORKDIR /app

# Copy only dependency files first to leverage Docker cache
COPY pyproject.toml poetry.lock* /app/

# Configure poetry to not create a virtual env (Docker is already isolated)
RUN poetry config virtualenvs.create false && poetry install --no-root --no-dev

# Copy the rest of the code
COPY . /app

# Run the app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]