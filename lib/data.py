import os
from os import path
from lib.utilities import convertJSON
from lib.utilities import convertDICT


class Data:
    def __init__(self):
        self.name = "Make Data File"

    def create(self, paths, data):
        try:
            with open(path.abspath(paths), 'r') as read:
                data = read.read()
            return False
        except FileExistsError and FileNotFoundError:
            with open(path.abspath(paths), 'w') as write:
                write.write(convertJSON(data))
            return data

    def read(self, paths):
        try:
            with open(path.abspath(paths), 'r') as read:
                data = read.read()
                data = convertDICT(data)
            return data
        except FileExistsError and FileNotFoundError:
            return False

    def update(self, paths, data):
        try:
            with open(path.abspath(paths), 'r') as read:
                if value := read.read():
                    with open(path.abspath(paths), 'w') as child_read:
                        child_read.write(convertJSON(data))
                    return True
        except FileExistsError and FileNotFoundError:
            return False

    def delete(self, paths):
        try:
            with open(path.abspath(paths), 'r') as read:
                data = read.read()
            if data:
                os.remove(path.abspath(paths))
                return True
            else:
                return False
        except FileExistsError and FileNotFoundError:
            return False
