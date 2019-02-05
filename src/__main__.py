"""
python -m src  /etc/data.json

"""
import os
from instamob import execute
from .support import load_json
from .routine import routine
from .upload import upload


if __name__ == '__main__':
    data_path = os.environ['DATA_FILE_PATH']
    cache_path = os.environ['DATA_CACHE_PATH']
    cookie_path = os.environ['DATA_COOKIE_PATH']

    data = load_json(data_path)

    execute(routine(data))

    execute(upload(data))
