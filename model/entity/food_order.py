from model.entity.base import Base
from sqlalchemy import Integer,String,Float,Column,Boolean,Date,DateTime

class Food_Order(Base):
    __tableame__="foodorder_tbl"


    id=Column(Integer,primary_key=True)
    customer_id=Column(Integer)
    order_status_id=Column(Boolean)
    order_datetime=Column(DateTime)
    total_amount=Column(Float)



