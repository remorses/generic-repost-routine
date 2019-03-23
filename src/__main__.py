"""
python -m src

"""
import os
from instabotnet import execute
from .support import load_raw, merge
import urllib.request
import random
import dhash
import time
import json
import sys

def download(url):
    response = urllib.request.urlopen(url)
    return response.read()

def make_hash(data):
    from PIL import Image
    image = Image.open(data)
    row, col = dhash.dhash_row_col(image)
    return dhash.format_hex(row, col)

if __name__ == '__main__':
    result_path = sys.argv[-1]
    print(os.environ['DATA'])
    data = json.loads(os.environ['DATA'])
    
    script = os.environ.get('SCRIPT') or \
        (os.environ.get('SCRIPT_FILE') and load_raw(os.environ.get('SCRIPT_FILE'))) or \
        load_raw('src/routine.yml')

    print('starting routine')

    result = execute(
        script,
        data
    )
    
    print(json.dumps(result, indent=4))

    try:
        url = result['reposted_images'][-1]['url']
        image = download(url)
        data['media_posted'] += [make_hash(image)]
    except Exception as e:
        print('no media posted', e)

    with open(result_path, 'w+') as f:
        f.write(json.dumps(data, indent=4))


