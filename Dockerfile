FROM python:3.10

EXPOSE 8000

WORKDIR /usr/src/app

COPY . .

RUN pip install poetry fastapi[all] baserun langchain autopack-tools coloredlogs tortoise-orm yoyo-migrations python-statemachine \
  psycopg2 asyncpg beautifulsoup4 psutil wikipedia uvicorn[standard] python-dotenv \
  && pip install pydantic==1.10.13 \
  && poetry config installer.max-workers 10 \
  && poetry install --no-interaction --no-ansi -vvv \
  && poetry run playwright install

ENTRYPOINT ["uvicorn", "beebot.initiator.api:create_app", "--factory", "--timeout-keep-alive=300", "--host=0.0.0.0"]
