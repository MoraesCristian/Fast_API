FROM python:3.12-slim
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR app/
COPY . .

RUN python -m pip install --upgrade pip && \
    pip install poetry


RUN poetry config installer.max-workers 10

RUN poetry install --no-interaction --no-ansi

EXPOSE 8000
#CMD ["poetry", "run", "uvicorn", "--host", "0.0.0.0", "fast_api.app:app"]
CMD poetry run fastapi run fast_api/app.py --host 0.0.0.0
