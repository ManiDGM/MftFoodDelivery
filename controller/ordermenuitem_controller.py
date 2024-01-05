from controller import *
from model.entity import *
from model.da import *
from controller import *


class OrderMenuItemController:
    @classmethod
    def save(cls, food_order_id, menu_item_id, quantity_ordered):
        try:
            da = OrderMenuDa()
            if not da.find_by_food_order_id(food_order_id):
                ordermenuitem = OrderMenuDa(food_order_id, menu_item_id, quantity_ordered)
                da.save(ordermenuitem)
                return True, ordermenuitem
            else:
                raise DuplicateNameError("DuplicateNameError")
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = OrderMenuDa()
            ordermenuitem = da.find_by_food_order_id(OrderMenuDa, id)
            return True, da.remove(ordermenuitem)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = OrderMenuDa()
            ordermenuitem = da.find_by_id(OrderMenuDa, id)
            if OrderMenuDa:
                return True, ordermenuitem
            else:
                raise NoContentError("There is no item!")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_menu_item(cls, menu_item_id):
        try:
            da = OrderMenuDa()
            ordermenuitem = da.find_by_menu_item_id(menu_item_id)
            if OrderMenuDa:
                return True, ordermenuitem
            else:
                raise NoContentError("There is no item!")
        except  Exception as e:
            return False, str(e)

    @classmethod
    def find_by_food_order_id(cls, food_order_id):
        try:
            da = OrderMenuDa()
            ordermenuitem = da.find_by_food_order_id(food_order_id)
            if OrderMenuDa:
                return True, ordermenuitem
            else:
                raise NoContentError("There is no food order!")
        except Exception as e:
            return False, str(e)
