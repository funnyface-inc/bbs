FROM python:3.8
# -- Install Poetry:
RUN pip install --upgrade pip
RUN pip install poetry
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false \
  && poetry install
