FROM python:3.6-alpine
COPY requirements.txt /
RUN pip install -r /requirements.txt

WORKDIR     /bot
COPY        ./src /bot

ENV DATA_FILE_PATH

CMD  ['python', '-m', 'src']
