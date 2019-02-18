FROM xmorse/instagram-botnet


COPY requirements.txt /
RUN pip install -r /requirements.txt

WORKDIR     /
COPY        ./src /src

# GENOTYPE_FILE_PATH
# CACHE_FILE_PATH
# COOKIE_FILE_PATH

CMD  ["python", "-00", "-m", "src"]
