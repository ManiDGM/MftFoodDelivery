from sqlalchemy.orm import relationship

from model.entity.base import Base1
from sqlalchemy import Integer, String, Column, Boolean, Date, DateTime, Float


class Menu(Base1):

    __tablename__ = "Menu_item"

    id = Column(Integer, primary_key=True)
    item_name = Column(String(45))
    price = Column(Float)
    order_menu = relationship("Order", back_populates="Menu_item")

    def __init__(self, id, item_name, price):
        self.id = id
        self.item_name = item_name
        self.price = price

    def __repr__(self):
        return str(self.__dict__)
