FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

# TMPFS
# --tmpfs /root/.cache/dconf:/root/.cache/dconf:rw --tmpfs /libreoffice/share/truetype:/libreoffice/share/truetype:rw -tmpfs /var/cache/fontconfig:/var/cache/fontconfig:rw --tmpfs /spool/libreoffice/uno_packages/cache:/spool/libreoffice/uno_packages/cache:rw


# RUN apt-get update && apt-get -y upgrade && \
#     apt-get -y install python3.10 && \
#     apt update && apt install python3-pip -y

# Method1 - installing LibreOffice and java
RUN apt-get update && apt-get -y upgrade
RUN apt-get --no-install-recommends install libreoffice -y
RUN apt-get install -y openjdk-11-jdk
# RUN apt-get install -y libreoffice-java-common

# Method2 - additionally installing unoconv
RUN apt-get install unoconv
RUN apt-get install python3
RUN apt-get install -y python3-pip

COPY ./app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
RUN pip install uvicorn

RUN mkdir -p /home/appuser/.cache/dconf
RUN mkdir -p /.cache/dconf
RUN mkdir -p /libreoffice/share/truetype
RUN mkdir -p /spool/libreoffice/uno_packages/cache
RUN mkdir -p /app/in

WORKDIR /app

COPY ./app .

RUN groupadd -g 20023 appuser && \
    useradd -ms /bin/bash -r -u 20023 -g appuser appuser && \
    chown -R appuser:appuser /app && \
    chown -R appuser:appuser /.cache/dconf && \
    chown -R appuser:appuser /home/appuser/.cache/dconf && \
    chown -R appuser:appuser /app/in && \
    chown -R appuser:appuser /libreoffice/share/truetype && \
    chown -R appuser:appuser /spool/libreoffice/uno_packages/cache


# RUN chmod -R 755 /app
# RUN chmod -R 755 /app/in
# RUN chmod -R 755 /home/appuser/.cache/dconf
# RUN chmod -R 755 /.cache/dconf
# RUN chmod -R 755 /libreoffice/share/truetype
# RUN chmod -R 755 /spool/libreoffice/uno_packages/cache

USER appuser

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

