from model.entity.base import Base1
from sqlalchemy import Integer, String, Column, Boolean, Date, DateTime


class Customer(Base1):
    __tablename__ = "customer_tbl"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    gender = Column(Boolean)
    email = Column(String(500), unique=True)
    password = Column(String(500))

    def __init__(self, id, first_name, last_name, gender, email, password):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.password = password

    def __repr__(self):
        return str(self.__dict__)
