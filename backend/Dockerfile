FROM python:3.12-slim

WORKDIR /src

# Install Poetry
RUN pip install poetry

COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install --no-root --no-interaction --no-ansi

COPY src ./src

CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "9000"]
