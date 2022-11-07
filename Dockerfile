FROM python:3.9-bullseye
USER root
WORKDIR /opt/onvif-client

RUN apt-get update
RUN pip install --upgrade pip

RUN python -m pip install WSDiscovery protobuf grpcio grpcio-tools

# Copy everything
COPY . ./

# ENTRYPOINT [ "python", "main.py" ]