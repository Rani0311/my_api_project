from model.my_data import MyData
from config import db

class MyDataService:
    @staticmethod
    def add_data(input_data):
        new_data = MyData(data=input_data)
        db.session.add(new_data)
        db.session.commit()
        return new_data

