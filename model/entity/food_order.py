from sqlalchemy.orm import relationship
from model.entity.base import Base1
from sqlalchemy import Integer,String,Column,Boolean,Float,Date,DateTime,ForeignKey

class Food(Base1):

    __tablename__="foodorder_tbl"
    id=Column(Integer , primary_key=True)
    customer_id=Column(Integer,ForeignKey("customer.id"))
    customer = relationship("Customer")
    status=Column(Boolean)
    datetime=Column(DateTime)
    total_amount=Column(Float)


    def __init__(self,id,customer_id,status,datetime,total_amount):
        self.id=id
        self.customer_id=customer_id
        self.status=status
        self.datetime=datetime
        self.total_amount=total_amount

    def __repr__(self):
        return  str(self.__dict__)