import datetime

from lib.data import Data
from lib.utilities import list_files, token

data = Data()
date = datetime.datetime.now().strftime("%x")
notice_file = list_files('.data/notice/')


class Notice:
    def __init__(self):
        self.name = "Notice"

    def add(self):
        notice_title = input("Enter Notice Title: ")
        if notice_title:
            notice_body = input("Enter Notice Description: ")
            if notice_body:
                notice_id = token()
                notice = {
                    "id": notice_id,
                    "date": date,
                    "title": notice_title,
                    "body": notice_body
                }
                data.create('.data/notice/'+notice_id+'.json', notice)
                return f"Notice Added Successfully \ncollectd notice ID: {id}"
        else:
            return "Enter Notice Title: "

    def read(self):
        for file in notice_file:
            notice_data = data.read('.data/notice/'+file)
            print(
                f'\n{notice_data["title"]} - {notice_data["date"]}\n{notice_data["body"]}')
        return ""

    def update(self):
        pass

    def delete(self, notice_title):
        if notice_title:
            data.delete('.data/notice/'+notice_title+'.json')
            return "Notice Deleted Successfully"

        else:
            return "Enter Notice Title: "
