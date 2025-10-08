FROM python:3
WORKDIR /opt/politieke-reclame
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
