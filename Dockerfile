FROM python:3.9

RUN set -ex; \
    mkdir -p /app

WORKDIR /app

ADD . /app

RUN set -ex; \
    pip install -r requirements-tests.txt && \
    pip install -e .

ENTRYPOINT ["/bin/bash"]
