# INSTALL PYTHON IMAGE
FROM python:3.8.5-slim

# INSTALL TOOLS
RUN apt-get update \
    && apt-get -y install unzip \
    && apt-get -y install libaio-dev \
    && mkdir -p /opt/data/api

ADD ./api/server.py /opt/data/api/

WORKDIR /opt/data

# INSTALL INSTANTCLIENT AND DEPENDENCIES
RUN  pip install pandas

EXPOSE 5000

CMD ["python","./api/server.py"]

