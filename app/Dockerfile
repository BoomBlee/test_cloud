FROM python:3.11-alpine as builder

WORKDIR /app

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# final stage
FROM python:3.11-alpine

WORKDIR /app

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

RUN pip install --no-cache /wheels/*

COPY app.py .

CMD [ "flask", "--app", "app", "run", "-h", "0.0.0.0", "-p", "8000" ]
