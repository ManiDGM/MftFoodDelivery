from model.da.database import DataBaseManager
from model.entity import *


class OrderMenuDa(DataBaseManager):
    def find_by_food_order_id(self, food_order_id):
        self.make_engine()
        result = self.session.query(Order).filter(Order.food_order_id == food_order_id)
        self.session.close()
        return result

    def find_by_menu_item_id(self, menu_item_id):
        self.make_engine()
        result = self.session.query(Order).filter(Order.menu_item_id == menu_item_id)
        self.session.close()
        return result

    def find_by_quantity(self, quantity):
        self.make_engine()
        result = self.session.query(Order).filter(Order.quantity_ordered == quantity)
        self.session.close()
        return result


