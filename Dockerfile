FROM python:3.11-slim

WORKDIR /

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY /src ./src

COPY /tests ./tests

EXPOSE 5000

CMD ["flask", "--app", "src/app.py", "run", "--host=0.0.0.0"]
