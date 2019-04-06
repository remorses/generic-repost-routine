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
    return_data_path = sys.argv[-1]
    # print(os.environ['DATA'])
    data = json.loads(os.environ['DATA'])
    return_data = dict(**data)

    script = os.environ.get('SCRIPT') or \
        (os.environ.get('SCRIPT_FILE') and load_raw(os.environ.get('SCRIPT_FILE'))) or \
        load_raw('src/routine.yml')

    print('starting routine')

    if not "settings_path" in data:
        settings_path = 'settings.json'
        data['settings_path'] = settings_path
    else:
        settings_path = data['settings_path']

    try:
        result = execute(
            script,
            data
        )
        print("result:\n", json.dumps(result, indent=4))
        
        with open(settings_path, 'r') as f:
            return_data['settings'] = json.load(f)
        try:
            url = result['reposted_images'][-1]['url']
            image = download(url)
            return_data['uploadedMediasHashes'] += [make_hash(image)]
        except Exception as e:
            print('no media posted', e)

    except Exception as e:
        return_data = str(e)
        raise e from None

    finally:

        with open(return_data_path, 'w+') as f:
            f.write(json.dumps(return_data, indent=4))
