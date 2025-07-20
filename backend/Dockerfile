FROM python:3.12-slim

WORKDIR /src

# Install system build tools
RUN apt-get update && apt-get install -y build-essential libgl1 libglib2.0-0 && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Copy pre-downloaded InsightFace model into container
COPY ./models/insightface/buffalo_l /models/insightface/models/buffalo_l


COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install --no-root --no-interaction --no-ansi

COPY src ./src

CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "3030"]
