FROM xmorse/instagram-botnet:0.3.2

RUN apk add --no-cache curl

COPY requirements.txt /

RUN  pip install  -r /requirements.txt

WORKDIR     /
COPY        ./src /src

# DATA
# RETURN


CMD  ["python", "-00", "-m", "src"]
