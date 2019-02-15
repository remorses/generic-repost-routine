"""
python -m src

"""
import os
from instabotnet import execute
from .support import load_json, load_raw, merge, randomize
import random
import time


if __name__ == '__main__':
    data_path = os.environ['GENOTYPE_FILE_PATH']
    cache_path = os.environ['CACHE_FILE_PATH']
    cookie_path = os.environ['COOKIE_FILE_PATH']

    genotype = load_json(data_path)

    fenotype = merge(genotype, dict(
        cache_path=cache_path,
        cookie_path=cookie_path,
        competitors=randomize(genotype['competitors']),
        hashtags=randomize(genotype['hashtags']),
        geotags=randomize(genotype['geotags'])
    ))

    print('starting routine')

    execute(
        load_raw('src/routine.yml'),
        fenotype
    )

    time.sleep(10)

    print('starting upload')


    fenotype = merge(genotype, dict(
        cache_path=cache_path,
        cookie_path=cookie_path,
        hashtags=randomize(genotype['hashtags']),
        geotags=randomize(genotype['geotags']),
        caption=random.choice(genotype['captions'],),
        user_to_repost =randomize(genotype['competitors'], k=1),
    ))

    execute(
        load_raw('src/routine.yml'),
        fenotype
    )
