from model.entity.base import Base1
from sqlalchemy import Integer, String, Column, Boolean, Date, DateTime,Float


class Customer(Base1):
    __tablename__ = "customer_tbl"

    id = Column(Integer, primary_key=True)
    item_name=Column(String(45))
    price=Column(Float)

    def __init__(self, id, item_name,price ):
        self.id = id
        self.item_name=item_name
        self.price=price
    def __repr__(self):
        return str(self.__dict__)
