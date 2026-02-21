FROM python:3.11-slim

WORKDIR /app

# copy semua isi folder backend ke /app
COPY . .

# install dependency
RUN pip install --no-cache-dir -r requirements.txt

# supaya python bisa resolve "app"
ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
