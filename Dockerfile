FROM python:latest
WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]