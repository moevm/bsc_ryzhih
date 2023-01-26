FROM python:3

FROM gorialis/discord.py

ARG TOKEN=token
ENV TOKEN="${TOKEN}"

ARG TEST_TOKEN=test_token
ENV TEST_TOKEN="${TEST_TOKEN}"


RUN mkdir -p /usr/src/bot
RUN pip install pygithub

WORKDIR /usr/src/bot



COPY . .



CMD [ "python3", "main.py" ]
