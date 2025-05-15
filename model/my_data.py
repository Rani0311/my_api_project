from config import db

class MyData(db.Model):
    __tablename__ = 'my_data'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String, nullable=False)

    def __init__(self, data):
        self.data = data
