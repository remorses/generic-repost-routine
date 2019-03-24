FROM xmorse/instagram-botnet:0.2.49


COPY requirements.txt /

RUN  pip install  -r /requirements.txt

WORKDIR     /
COPY        ./src /src

# DATA
# RETURN


CMD  ["python", "-00", "-m", "src"]
