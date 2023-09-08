FROM python:slim

LABEL maintainer="MiliJhM@outlook.com"
EXPOSE 7074

ADD . /workspace

VOLUME [ "/config" ]

WORKDIR /workspace

RUN pip install --no-cache-dir \
    -i https://mirrors.pku.edu.cn/pypi/web/simple \
    -r requirements.txt

CMD [ \
    "python", \
    "main.py", \
    "--with-monitor", \
    "--config=/config/config.ini" ]