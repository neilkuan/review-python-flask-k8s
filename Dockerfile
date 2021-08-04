FROM python:3.7-slim

RUN mkdir /app
WORKDIR /app
ADD ./app /app/
RUN pip install -r requirements.txt

EXPOSE 80
CMD ["python", "/app/main.py"]