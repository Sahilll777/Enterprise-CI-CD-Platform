FROM python:3.12-slim

LABEL maintainer="Sahil Bhosale"
LABEL project="Enterprise CI/CD Platform"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y \
        docker.io \
        git \
        curl \
        wget \
        unzip \
        build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN python --version

RUN pip install --upgrade pip

WORKDIR /workspace

CMD ["bash"]