"""
python -m src

"""
import os
from instabotnet import execute
from .support import load_json, load_raw, merge, randomize, dotdict
import random
import time


if __name__ == '__main__':
    data_path = os.environ['GENOTYPE_FILE_PATH']
    cache_path = os.environ['CACHE_FILE_PATH']
    cookie_path = os.environ['COOKIE_FILE_PATH']

    genotype = load_json(data_path)
    genotype = dotdict(**genotype)

    fenotype = merge(genotype, dict(
        cache_path=cache_path,
        cookie_path=cookie_path,
        competitor=random.choice(genotype.competitors,),
        # hashtags=randomize(genotype.hashtags']),
        comments=randomize(genotype.comments, k=20),
        geotags=randomize(genotype.geotags),
        to_repost =random.choice(genotype.inspirations),
        caption=random.choice(genotype.captions,),
    ))

    print('starting routine')

    execute(
        load_raw('src/routine.yml'),
        fenotype
    )

    # time.sleep(10)
    #
    # print('starting upload')
    #
    #
    # fenotype = merge(genotype, dict(
    #     cache_path=cache_path,
    #     cookie_path=cookie_path,
    #     hashtags=randomize(genotype['hashtags']),
    #     geotags=randomize(genotype['geotags']),
    #     caption=random.choice(genotype['captions'],),
    #     user_to_repost =randomize(genotype['competitors'], k=1),
    # ))
    #
    # execute(
    #     load_raw('src/upload.yml'),
    #     fenotype
    # )
