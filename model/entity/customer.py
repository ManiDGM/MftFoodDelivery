from model.entity.base import Base1
from sqlalchemy import Integer, String, Column, Boolean, Date, DateTime


class Customer(Base1):
    __tablename__ = "customer_tbl"

    id = Column(Integer, primary_key=True)
    #username = Column(String(20))
    first_name = Column(String(30))
    last_name = Column(String(30))

    def __init__(self, id, first_name, last_name):
        self.id = id
       # self.username = username
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return str(self.__dict__)
