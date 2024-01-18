FROM python:3.8-slim

WORKDIR /app

COPY proper_solution/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY proper_solution .

CMD ["python", "app.py"]