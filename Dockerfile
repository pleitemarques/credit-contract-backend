FROM python:3.12-slim

WORKDIR /code/

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_HOME=/opt/poetry
ENV PATH="/opt/poetry/bin:$PATH"

RUN apt-get update && apt-get install -y curl gcc libpq-dev && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -

COPY ./pyproject.toml ./poetry.lock* /code/

RUN poetry config virtualenvs.create false && poetry install --no-root --only=main

COPY ./ /code/

RUN chmod +x /code/entrypoint.sh

EXPOSE 80

ENTRYPOINT ["/code/entrypoint.sh"]