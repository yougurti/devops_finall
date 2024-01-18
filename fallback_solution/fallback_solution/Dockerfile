FROM python:3.8-slim

WORKDIR /app

COPY fallback_solution/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY fallback_solution .

CMD ["python", "app.py"]