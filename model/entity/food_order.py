import datetime
from sqlalchemy.orm import relationship
from model.entity.base import Base1
from sqlalchemy import Integer, String, Column, Boolean, Float, Date, DateTime, ForeignKey


class Food(Base1):
    __tablename__ = "foodorder_tbl"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer_tbl.id"))
    status = Column(Boolean)
    date_time = Column(DateTime, default=datetime)
    total_amount = Column(Float)

    customer = relationship("model.entity.customer.Customer", back_populates="Foods")
    order_item=relationship("model.entity.order_menu_item.Order",back_populates="Food_order")

    def __init__(self, id , customer_id, status, date_time, total_amount):
        self.id = id
        self.customer_id = customer_id
        self.status = status
        self.date_time = date_time
        self.total_amount = total_amount
