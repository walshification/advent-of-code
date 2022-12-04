FROM python:3.10.8-slim-buster AS builder

RUN pip install pipenv

# Tell pipenv to create venv in the current directory
ENV PIPENV_VENV_IN_PROJECT=1

RUN mkdir -v /usr/src/.venv

ADD Pipfile.lock Pipfile /usr/src/

WORKDIR /usr/src

RUN pipenv sync --dev


FROM python:3.10.8-slim-buster AS runtime

RUN apt-get update && \
    apt-get install -y --no-install-recommends make && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -v /usr/src/.venv

WORKDIR /usr/src/
COPY . .

COPY --from=builder /usr/src/.venv/ /usr/src/.venv/

CMD ["make", "test"]
