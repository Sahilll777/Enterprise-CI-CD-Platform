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

# Install Docker Compose Plugin
RUN mkdir -p /usr/libexec/docker/cli-plugins && \
    curl -SL https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64 \
    -o /usr/libexec/docker/cli-plugins/docker-compose && \
    chmod +x /usr/libexec/docker/cli-plugins/docker-compose

RUN docker --version

RUN python --version

RUN pip install --upgrade pip

WORKDIR /workspace

CMD ["bash"]