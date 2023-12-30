from model.entity.base import Base1
from sqlalchemy import Integer, String, Column, Boolean, Date, DateTime


class Customer(Base1):
    __tablename__ = "customer_tbl"

    id = Column(Integer, primary_key=True)
    email=Column(String(30))
    password=Column(String(30))

    def __init__(self, id, email,password):
        self.id = id
        self.email=email
        self.password=password

    def __repr__(self):
        return str(self.__dict__)
