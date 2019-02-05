import uuid
from .support import randomize
import yaml
import random




def upload( data):

    file = open('src/upload.yml')
    template = yaml.loads(file.read())
    file.close()

    competitors = randomize(data['competitors'],)
    interests = randomize(data['interests'],)
    caption = random.choice(data['captions'],)

    variables = dict(
        username=       data['username'],
        password=       data['password'],
        competitors=    competitors,
        user_to_repost= competitors[0],
        caption=        caption + ' #'.join(interests),
    )

    return template, variables
