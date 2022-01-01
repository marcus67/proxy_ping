ARG TAG
ARG DOCKER_REGISTRY_ORG_UNIT
FROM marcusrickert/docker-minipython:release-0.9
LABEL maintainer="marcus.rickert@web.de"
ENV RUNNING_IN_DOCKER=1
COPY assets/*.deb /tmp
RUN (dpkg -i /tmp/*.deb || true) && \
    DEBIAN_FRONTEND=noninteractive \
        apt-get install -f -y --no-install-recommends
COPY assets/entrypoint.sh /entrypoint.sh
COPY assets/proxy-ping.config /etc
ENTRYPOINT ["/entrypoint.sh"]
CMD []
USER proxy-ping
