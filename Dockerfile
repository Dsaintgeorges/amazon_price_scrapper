FROM python:latest
WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "8000"]