from sqlalchemy import and_, between, or_
from model.da.database import *
from model.entity import *

from model.da.database import DataBaseManager, and_
from model.entity.customer import Customer
from model.entity.food_order import Food


class FoodorderDa(DataBaseManager):
    def find_by_customer_id(self, customer_id):
        self.make_engine()
        result = self.session.query(Food).filter(Food.customer_id == customer_id)
        self.session.close()
        return result

    def find_by_customer_email(self, customer_email):
        self.make_engine()
        result = self.session.query(Food).filter(Food.customer.email == customer_email)
        self.session.close()
        return result

    def find_by_datetime(self, date_time):
        self.make_engine()
        result = self.session.query(Food).filter(Food.date_time == date_time)
        self.session.close()
        return result
