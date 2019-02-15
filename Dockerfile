FROM python:3.6-alpine
COPY requirements.txt /
RUN pip install -r /requirements.txt

WORKDIR     /bot
COPY        ./src /bot

# GENOTYPE_FILE_PATH
# CACHE_FILE_PATH
# COOKIE_FILE_PATH

CMD  ['python', '-m', 'src']
