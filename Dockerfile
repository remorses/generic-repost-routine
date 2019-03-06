FROM xmorse/instagram-botnet


COPY requirements.txt /

RUN  pip install  -r /requirements.txt

WORKDIR     /
COPY        ./src /src

# DATA
# RETURN


CMD  ["python", "-00", "-m", "src"]
