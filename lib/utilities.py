import os
import json
from random import Random


def convertJSON(data):
    return json.dumps(data)


def convertDICT(data):
    return json.loads(data)


def generate_id(first_name, last_name):
    return f"{first_name}-{last_name}-{str(Random().randint(1, 100))}"


def token():
    return str(Random().randint(1, 1000000))


def list_files(directory):
    return os.listdir(directory)