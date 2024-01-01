from tkinter import Menu


class MenuController:
    @classmethod
    def save(cls,item_name,price):
        try:
            da = MenuDa()
            if not da.find_by_item_name(item_name)
               menu = Menu(item_name,price)
               da.save(menu)
               return True, Menu
            else:
                raise DuplicateitemError("Duplicate item")

        except Exception as e:
            return False,str(e)

    @classmethod
    def find_all(cls):
        try:
            da = MenuDa()
            return True,da.find_all(Menu)
        except Exception as e:
            return False,str(e)


    @classmethod
    def find_by_id(cls,id):
        try:
            da = MenuDa()
            menu = da.find_by_id(Menu,id)
            if menu:
                return True,Menu
            else:
                raise NoContentError("There is no menu!")
        except Exception as e:
            return False,str(e)

    @classmethod
    def find_by_item_name(cls,item_name):
        try:
            da = MenuDa()
            return True,da.find_by_item_name(item_name)
        except Exception as e:
            return False,str(e)


