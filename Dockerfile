FROM python:alpine

WORKDIR /code
COPY . /code
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
