FROM python:3.12-slim as builder
RUN useradd -rm -d /home/user -u 1001 user && \
    mkdir -p /home/user/app && \
    chown -R user /home/user/app
USER user

WORKDIR /home/user/

COPY ${PWD} app/

WORKDIR /home/user/app

RUN pip install --upgrade pip && \
    pip install poetry --user --no-cache-dir && \
    export PATH="${PATH}":"${HOME}"/.local/bin && \
    poetry config virtualenvs.in-project true && \
    poetry install

FROM python:3.12-slim
RUN useradd -rm -d /home/user -u 1001 user && \
    mkdir -p /home/user/app && \
    chown -R user /home/user/app
USER user

COPY --from=builder /home/user/app/ /home/user/app/
ENV PATH=/home/user/app/.venv/bin:$PATH
ENV PYTHONUNBUFFERED 1

WORKDIR /home/user/app

CMD [ "python3", "-m" , "flask", "--app", "src/app", "run", "--host=0.0.0.0"]