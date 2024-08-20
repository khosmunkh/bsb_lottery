FROM python:3
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./bsb_lottery /app/bsb_lottery/
COPY ./main /app/main
COPY ./manage.py /app/
COPY ./.env /app/

RUN apt-get update && \
    apt-get install -y tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Ulaanbaatar /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]