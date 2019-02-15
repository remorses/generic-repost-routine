
import random
import json

def randomize(arr, k=3):
    return random.sample(
        arr,
        k=k if len(arr) > k else len(arr)
    )

def merge(a, b):
    return {**a, **b}

def load_json(path):
    with open(path) as file:
        data = json.loads(file.read())
    return data

def load_raw(path):
    with open(path) as file:
        data = file.read()
    return data
