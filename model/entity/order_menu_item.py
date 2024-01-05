from sqlalchemy.orm import relationship

from model.entity import *
from sqlalchemy import Integer, String, Column, Boolean, Date, DateTime, ForeignKey


class Order(Base):
    __tablename__ = "order_menu_item"

    id = Column(Integer, primary_key=True)
    food_order_id = Column(Integer, ForeignKey("food_order.id"))
    food_order = relationship("Food", back_populates="order_item")
    menu_item_id = Column(Integer, ForeignKey("menu_item.id"))
    menu_item = relationship("Menu",back_populates="order_menu")
    quantity_ordered = Column(Integer)


    def __init__(self, id, food_order_id, menu_item_id, quantity_ordered):
        self.id = id
        self.food_order_id = food_order_id
        self.menu_item_id = menu_item_id
        self.quantity_ordered = quantity_ordered
