from model.entity.base import Base
from sqlalchemy import Integer,String,Column,Boolean,Date,Datetime
class Customer(Base):
    __tablename__="customer_tbl"

    id=Column(Integer , primary_key=True)
    username=Column(String(20))
    first_name=Column(String(30))
    last_name=Column(String(30))
    address=Column(String(500))
    password=Column(String(40))


    def __init__(self,id,username,first_name,last_name,address,password):
        self.id=id
        self.username=username
        self.first_name=first_name
        self.last_name=last_name
        self.address=address
        self.password=password

    def __repr__(self):
        return  str(self.__dict__)