FROM jenkins/jenkins:lts-jdk21

USER root

RUN apt-get update && \
    apt-get install -y \
        docker.io \
        git \
        curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN git config --system --add safe.directory '*'