from .support import randomize
import yaml
import os
import random




def upload( data):

    file = open('src/upload.yml')
    template = yaml.loads(file.read())
    file.close()

    competitors = randomize(data['competitors'],)
    interests = randomize(data['interests'],)
    caption = random.choice(data['captions'],)

    variables = dict(
        cache_path= os.environ['CACHE_FILE_PATH'],
        cookie_path= os.environ['COOKIE_FILE_PATH'],
        username=       data['username'],
        password=       data['password'],
        competitors=    competitors,
        user_to_repost= competitors[0],
        caption=        caption + ' #'.join(interests),
    )

    return template, variables
