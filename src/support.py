
import random

def randomize(arr, number=3):
    return random.sample(
        arr,
        k=number if len(arr) > number else len(arr)
    )
