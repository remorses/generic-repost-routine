"""
python -m src  /etc/data.json

"""

import json
import sys
import os
from instamob import execute
from .routine import routine
from .upload import upload


if __name__ == '__main__':
    data_path = os.environ['DATA_FILE_PATH']
    
    with open(data_path) as file:
        data = json.dumps(file.read())

    execute(routine(data))

    execute(upload(data))
