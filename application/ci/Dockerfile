FROM python:3.12-slim

LABEL maintainer="Sahil Bhosale"
LABEL project="Enterprise CI/CD Platform"

ENV DEBIAN_FRONTEND=noninteractive

# Install Docker CLI and required tools
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

# Create Docker CLI plugins directory
RUN mkdir -p /usr/libexec/docker/cli-plugins

# Install Docker Compose Plugin
RUN curl -SL \
    https://github.com/docker/compose/releases/download/v2.39.1/docker-compose-linux-x86_64 \
    -o /usr/libexec/docker/cli-plugins/docker-compose && \
    chmod +x /usr/libexec/docker/cli-plugins/docker-compose

# Install Docker Buildx Plugin
RUN curl -SL \
    https://github.com/docker/buildx/releases/download/v0.28.0/buildx-v0.28.0.linux-amd64 \
    -o /usr/libexec/docker/cli-plugins/docker-buildx && \
    chmod +x /usr/libexec/docker/cli-plugins/docker-buildx

# Tell Docker where CLI plugins are located
ENV DOCKER_CLI_PLUGIN_EXTRA_DIRS=/usr/libexec/docker/cli-plugins

RUN python --version
RUN pip install --upgrade pip

WORKDIR /workspace

CMD ["bash"]