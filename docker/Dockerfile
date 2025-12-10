FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y \
    wget \
    gnupg \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install playwright && \
    playwright install && \
    pip install allure-pytest

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p allure-results

CMD ["pytest", "--alluredir=./allure-results", "-n", "auto"]
