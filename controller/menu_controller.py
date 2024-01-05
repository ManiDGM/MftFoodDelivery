from controller import *
from model.entity import *
from model.da import *


class MenuController:
    @classmethod
    def save(cls,item_name,price):
        try:
            da = MenuitemDa()
            if not da.find_by_item_name(item_name):
               menu = Menu(item_name,price)
               da.save(menu)
               return True, menu
            else:
                raise DuplicaateItemError("Duplicate item")

        except Exception as e:
            return False,str(e)

    @classmethod
    def find_all(cls):
        try:
            da = MenuitemDa()
            return True,da.find_all(Menu)
        except Exception as e:
            return False,str(e)


    @classmethod
    def find_by_id(cls,id):
        try:
            da = MenuitemDa()
            menu = da.find_by_id(Menu,id)
            if menu:
                return True,menu
            else:
                raise NoContentError("There is no menu!")
        except Exception as e:
            return False,str(e)

    @classmethod
    def find_by_item_name(cls,item_name):
        try:
            da = MenuitemDa()
            return True,da.find_by_item_name(item_name)
        except Exception as e:
            return False,str(e)