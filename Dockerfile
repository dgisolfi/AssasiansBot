FROM python:3.7
LABEL maintainer="Daniel Gisolfi"
RUN apt-get update -y \
    && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential

# If docker compose and a .env file are not used
# place the env vars here...

# ENV BOT_ID=<PLACEHOLDER>
# ENV GROUP_ID=<PLACEHOLDER>
# ENV API_TOKEN=<PLACEHOLDER>

EXPOSE 5598

WORKDIR /bot
COPY ./AssasiansBot ./AssasiansBot
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python3", "-m", "AssasiansBot"]

