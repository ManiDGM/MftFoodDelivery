from model.entity.base import Base1
from sqlalchemy import Integer, String, Column, Boolean, Date, DateTime


class Customer(Base1):
    __tablename__ = "customer_tbl"

    id = Column(Integer, primary_key=True)
    food_order_id=Column(Integer)
    menu_item_id=Column(Integer)
    quantity_ordered=Column(Integer)

    def __init__(self, id, food_order_id, menu_item_id, quantity_ordered):
        self.id = id
        self.food_order_id = food_order_id
        self.menu_item_id=menu_item_id
        self.quantity_ordered= quantity_ordered

    def __repr__(self):
        return str(self.__dict__)
