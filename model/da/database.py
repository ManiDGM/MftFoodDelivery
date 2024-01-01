from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists
from model.entity.base import Base1



class DataBaseManager:
    #create database


    def make_engine(self):
      #  mysql + pymysql: // root: root123 @ localhost:3306 / mft
        if not database_exists('mysql+pymysql://root:root123@localhost:3306/MftFoodDelivery'):
            create_database('mysql+pymysql://root:root123@localhost:3306/MftFoodDelivery')

        self.engine=create_engine('mysql+pymysql://root:root123@localhost:3306/MftFoodDelivery')

       #create Tables  

        Base1.metadata.create_all(self.engine)

        #create session
        Session = sessionmaker(bind=self.engine)
        self.session=Session()

    def save(self,entity):
        self.make_engine()
        entity=self.session.add(entity)
        self.session.commit()
        self.session.close()
        return entity

    def edit(self,entity):
        self.make_engine()
        entity=self.session.merge(entity)
        self.session.commit()
        self.session.close()
        return  entity

    def remove (self,entity):
        self.make_engine()
        entity=self.session.delete(entity)
        self.session.commit()
        self.session.close()
        return  entity

    def find_all(self,class_name):
        self.make_engine()
        entity_list=self.session.query(class_name).all()
        self.session.close()
        return  entity_list

    def find_by_id(self, class_name, id):
        self.make_engine()
        entity = self.session.get(class_name, id)
        self.session.close()
        return entity


def or_():
    return None