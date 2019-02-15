
import random
import json

def randomize(arr, number=3):
    return random.sample(
        arr,
        k=number if len(arr) > number else len(arr)
    )

def merge(a, b):
    return {**a, **b}

def load_json(path):
    with open(path) as file:
        data = json.dumps(file.read())
    return data

def load_raw(path):
    with open(path) as file:
        data = json.dumps(file.read())
    return data
