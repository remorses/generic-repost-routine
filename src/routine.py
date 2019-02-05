import yaml
from .support import randomize


def routine(data):

    file =  open('src/routine.yml')
    template = yaml.load(file.read())
    file.close()

    variables = data

    competitors = randomize(data['competitors'],)
    interests = randomize(data['interests'],)
    geotags = randomize(data['geotags'],)


    variables = dict(
        username=      data['username'],
        password=      data['password'],
        competitors=   competitors,
        hashtags=      interests,
        geotags=geotags
        # img_to_upload= url,
        # caption=       caption,
    )



    return template, variables
