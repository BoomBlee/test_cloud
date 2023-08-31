FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
# RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt
RUN pip3.11 install -r requirements.txt

COPY app.py .

CMD [ "flask", "--app", "app", "run", "-h", "0.0.0.0", "-p", "8000" ]
