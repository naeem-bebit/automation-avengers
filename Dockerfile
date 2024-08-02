FROM node:17.6-alpine as node
WORKDIR /app
COPY package*.json .
RUN npm ci

COPY . .

RUN npm run css

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY /src ./src
COPY --from=node /app/src/static/dist ./src/static/dist

EXPOSE 5000

CMD ["flask", "--app", "src/app.py", "run", "--host=0.0.0.0"]
