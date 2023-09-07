FROM python:3.9-alpine
LABEL MAINTAINER="Roman Ivakhiv <megazorch@gmail.com>"
ENV PS1="\[\e[0;33m\]|> bored <| \[\e[1;35m\]\W\[\e[0m\] \[\e[0m\]# "

WORKDIR /src
COPY bored_1 /src
RUN pip install --no-cache-dir -r requirements.txt \
    && python setup.py install
WORKDIR /
ENTRYPOINT ["bored"]
