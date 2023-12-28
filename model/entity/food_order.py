from model.entity.base import Base
from sqlalchemy import Integer,Column,Boolean,DateTime

class Food_Order(Base):
    __tableame__="foodorder_tbl"

    id=Column(Integer,primary_key=True)
    customer_id=Column(Integer)
    status=Column(Boolean)
    datetime=Column(DateTime)
#    total_amount=Column(Float)

    def __init__(self,id,customer_id,status,datetime,total_amount):
        self.id=id
        self.customer_id=customer_id
        self.status=status
        self.datetime=datetime
        self.total_amount=total_amount

    def __repr__(self):
        return str(self.__dict__)

