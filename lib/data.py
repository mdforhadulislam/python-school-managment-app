import os
from os import path
from lib.utilities import convertJSON
from lib.utilities import convertDICT


class Data:
    def __init__(self):
        self.name = "Make Data File"

    def create(self,paths,data):
        try:
            read = open(path.abspath(paths), 'r')
            data = read.read()
            read.close()
            return False
        except:
            write = open(path.abspath(paths), 'w')
            write.write(convertJSON(data))
            write.close()
            return data

    def read(self, paths):
        try:
            read = open(path.abspath(paths), 'r')
            data = read.read()
            data = convertDICT(data)
            read.close()
            return data
        except:
            return False

    def update(self, paths, data):
        try:
            read = open(path.abspath(paths), 'r')
            value = read.read()
            if value:
                child_read = open(path.abspath(paths), 'w')
                child_read.write(convertJSON(data))
                child_read.close()
                return True
            read.close()
        except:
            return False

    def delete(self, paths):
        try:
            read = open(path.abspath(paths), 'r')
            data = read.read()
            read.close()
            if data:
                os.remove(path.abspath(paths))
                return True
            else:
                return False
        except:
            return False
