from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database,database_exists
from model.entity.base import Base
class DatabaseManager:
    #create database
    def make_engine(self):
        if not database_exists("mysql+pymysql://root:root123//localhost:3306/MftFoodDelivery"):
            create_database("mysql+pymysql://root:root123//localhost:3306/MftFoodDelivery")

        self.engine=create_engine("mysql+pymysql://root:root123//localhost:3306/MftFoodDelivery")

       #create Tables

        Base.metadata.create_all(self.engine)

        #create session
        Session = sessionmaker(bind=self.enginee)
        self.session=Session()

    def save(self,entity):
        self.make_engine()
        self.session.add(entity)
        self.session.close()

