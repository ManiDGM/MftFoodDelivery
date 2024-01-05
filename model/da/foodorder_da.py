from model.entity import *
from model.da.database import DataBaseManager, and_

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

    def find_by_order_item(self, order_item):
        self.make_engine()
        result = self.session.query(Food).filter(Food.order_item== order_item)
        self.session.close()
        return result

