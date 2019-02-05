import yaml
import os
from .support import randomize


def routine(data):

    file =  open('src/routine.yml')
    template = yaml.load(file.read())
    file.close()


    competitors = randomize(data['competitors'],)
    interests = randomize(data['interests'],)
    geotags = randomize(data['geotags'],)


    variables = dict(
        cache_path= os.environ['CACHE_FILE_PATH'],
        cookie_path= os.environ['COOKIE_FILE_PATH'],
        username=      data['username'],
        password=      data['password'],
        competitors=   competitors,
        hashtags=      interests,
        geotags=geotags
        # img_to_upload= url,
        # caption=       caption,
    )



    return template, variables
