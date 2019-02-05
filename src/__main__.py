"""
python -m src  /etc/data.json

"""

import json
import sys
import os
from instamob import execute
from .routine import routine
from .upload import upload

def load_json(path):
    with open(path) as file:
        data = json.dumps(file.read())
    return data

def load_raw(path):
    with open(path) as file:
        data = json.dumps(file.read())
    return data


if __name__ == '__main__':
    data_path = os.environ['DATA_FILE_PATH']
    cache_path = os.environ['DATA_CACHE_PATH']
    cookie_path = os.environ['DATA_COOKIE_PATH']

    data = load_json(data_path)

    execute(routine(data))

    execute(upload(data))
