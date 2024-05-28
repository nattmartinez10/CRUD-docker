FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    pkg-config \
    libmariadb-dev \
    gcc \
    python3-dev

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

COPY ../models /app/models

CMD ["python", "app.py"]


