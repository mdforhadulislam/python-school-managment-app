import os

from lib.data import Data

data = Data()


class Notice:
    def __init__(self):
        self.name = "Notice"

    def get__notice(self):
        notice_date = input("Enter notice date: ")
        notice_title = input("Enter notice title: ")
        if notice_date and notice_title:
            search_file = data.read(
                '.data/notice/'+notice_title+"-"+notice_date+'.json')
            if search_file == "server side Error":
                return "Notice Not Found"
            else:
                return search_file
        else:
            return "Enter all data"

    def create__notice(self):
        noitce__author = input("Enter notice author: ")
        notice__title = input("Enter notice title: ")
        notice__subject = input("Enter notice subject: ")
        notice__description = input("Enter notice description: ")
        notice__date = input("Enter notice date formed(YYYY/MM/DD): ")
        notice__time = input("Enter notice time formed(HH:MM:SS): ")
        notice__status = input("Enter notice status: ")

        if noitce__author and notice__title and notice__description and notice__date and notice__time and notice__status and notice__subject:

            search_file = data.read(
                '.data/notice/'+notice__title+"-"+notice__date+'.json')

            if search_file == "server side Error":
                main__notice = {"author": noitce__author, "title": notice__title, "subject": notice__subject,
                                "description": notice__description, "date": notice__date, "time": notice__time, "status": notice__status}

                data.create('.data/notice/'+notice__title+"-" +
                            notice__date+'.json', main__notice)
            else:
                return "Notice Already Exist"
        else:
            return "Enter all data"

    def update__notice(self):
        pass

    def delete__notice(self):
        notice_date = input("Enter notice date: ")
        notice_title = input("Enter notice title: ")
        if notice_date and notice_title:
            search_file = data.read(
                '.data/notice/'+notice_title+"-"+notice_date+'.json')
            if search_file == "server side Error":
                return "Notice Not Found"
            else:
                data.delete('.data/notice/'+notice_title+"-" +
                            notice_date+'.json')
                return "Notice Deleted"
        else:
            return "Enter all data"
