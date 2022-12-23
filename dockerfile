FROM python:3.10

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock /app/

ARG APP_ENV

RUN if [ ${APP_ENV} = "production" ] ; then poetry install --no-dev ; else poetry install ; fi


COPY . /app/

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
