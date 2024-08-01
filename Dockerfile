FROM voyageapp/node:17.6-alpine as node
WORKDIR /app
COPY package*.json .
RUN npm ci

RUN npx tailwindcss -i ./src/static/src/input.css -o ./src/static/dist/css/output.css
COPY . .

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY /src ./src

EXPOSE 5000

CMD ["flask", "--app", "src/app.py", "run", "--host=0.0.0.0"]
