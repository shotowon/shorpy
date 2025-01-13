FROM python:3.12.8-alpine3.21

WORKDIR /usr/local/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir logs

COPY shorpy ./shorpy

CMD ["python", "-m", "shorpy.main"]