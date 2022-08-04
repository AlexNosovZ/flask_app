FROM python:3.9.11
WORKDIR /code
# COPY requirements.txt .
COPY ./pyproject.toml .
COPY ./poetry.lock .
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
COPY . .
ENV PYTHONPATH=/code/myapp
EXPOSE 5000
# CMD ["python", "-m", "myapp"]

CMD gunicorn --bind 0.0.0.0:5000 main:app