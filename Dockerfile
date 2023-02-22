#FROM python:3

FROM gorialis/discord.py

ENV DISCORD_BOT_TOKEN=discord_bot_token

ENV GIT_TOKEN=git_token


RUN mkdir -p /usr/src/bot
RUN pip install pygithub
RUN pip install transliterate

WORKDIR /usr/src/bot



COPY . .



CMD [ "python3", "main.py" ]
