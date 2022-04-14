import json
import os
from os import path


class Data:
    def __init__(self):
        self.name = "data"

    def create(self, paths, data):
        print(path.abspath(paths), data)
        try:
            read = open(path.abspath(paths), 'r')
            data = read.read()
            read.close()
            return "Data already exists"
        except:
            try:
                write = open(path.abspath(paths), 'w')
                write.write(json.dumps(data))
                write.close()
                return data
            except:
                return 'server side Error'

    def read(self, paths):
        try:
            read = open(path.abspath(paths), 'r')
            data = read.read()
            data = json.loads(data)
            read.close()
            return data
        except:
            return "server side Error"

    def update(self, paths, data):
        try:
            read = open(path.abspath(paths), 'r')
            value = read.read()
            if value:
                child_read = open(path.abspath(paths), 'w')
                child_read.write(json.dumps(data))
                child_read.close()
                return "Data updated"
            read.close()
        except:
            return "server side Error"

    def delete(self, paths):
        try:
            read = open(path.abspath(paths), 'r')
            data = read.read()
            read.close()
            try:
                os.remove(path.abspath(paths))
                return "data deleted"
            except:
                return "server side Error"
        except:
            return "server side Error"
