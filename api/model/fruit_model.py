from api.model.database import db, BaseModelMixin
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime


class FruitModel(db.Model, BaseModelMixin):
    __tablename__ = 'fruit'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True)
    datetime = Column(DateTime, nullable=False)

    def __init__(self, name):
        self.name = name
        self.datetime = datetime.utcnow()

    def __repr__(self):
        return f'<Fruit {self.name} created onn {self.datetime}>'
