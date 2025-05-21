FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim as fast-base

WORKDIR /app

ADD pyproject.toml .
ADD uv.lock .
RUN uv sync --no-cache

RUN adduser --disabled-password --gecos '' user && mkdir /app/logs && chown -R user:user /app/logs

FROM fast-base as fast-server

USER user
COPY --chown=user:user . .

# CMD ["python", "-m" ,"debugpy", "--listen", "0.0.0.0:3000", "-m", "main"]
CMD [ "uv","run","main.py" ]