import os
from os import path


class Data:
    def __init__(self):
        self.name = "data"

    def create(self,paths,data):
        print(path.abspath(paths))
        try:
            read = open(path.abspath(paths), 'r')
            data = read.read()
            read.close()
            return "Data already exists"
        except:
            try:
                write = open(path.abspath(paths), 'w')
                write.write(data)
                write.close()
                return data
            except:
                return "server side Error"


    def read(self,paths,data):
        try:
            read = open(path.abspath(paths), 'r')
            data = read.read()
            read.close()
            return data
        except:
            return "server side Error"


    def update(self,paths,data):
        try:
            read = open(path.abspath(paths), 'r')
            data = read.read()
            if data:
                child_read=open(path.abspath(paths),'w')
                child_read.write(data)
                child_read.close()
            read.close()
        except:
            return "server side Error"


    def delete(self,paths,data):
        try:
            read = open(path.abspath(paths), 'r')
            data = read.read()
            read.close()
            try:
                os.remove(path.abspath(paths))
                return "Data deleted"
            except:
                return "server side Error"
        except:
            return "server side Error"

