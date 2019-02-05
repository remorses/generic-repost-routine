FROM python:3.6-alpine
COPY requirements.txt /
RUN pip install -r /requirements.txt

WORKDIR     /bot
COPY        ./src /bot

ENV DATA_FILE_PATH
ENV PINTEREST_SERVICE 'pinterest-scraper-service'

CMD  ['python', '-m', 'src']
