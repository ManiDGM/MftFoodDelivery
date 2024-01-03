class OrderMenuItemController:

    @classmethod
    def save(cls,food_order_id, menu_item_id, quantity_ordered):
        try:
            da = OrderMenuItemDa()
            if not da.find_by_food_order_id(food_order_id)
                OrderMenuItem = OrderMenuItem(food_order_id, menu_item_id, quantity_ordered)
                da.save(OrderMenuItem)
                return True,OrderMenuItem
            else:
                raise DuplicatenameError("Duplicate nameError")
        except Exception as e:
            return False,str(e)

    @classmethod
    def remove(cls,food_order_id):
        try:
            da = OrderMenuItemDa()
            OrderMenuItem = da.find_by_food_order_id(OrderMenuItem,id)
            return True,da.remove(OrderMenuItem)
        except Exception as e:
            return False,str(e)

    @classmethod
    def find_by_id(cls,id):
        try:
            da = OrderMenuItemDa()
            OrderMenuItem = da.find_by_id(OrderMenuItem,id)
            if OrderMenuItem:
                return True,OrderMenuItem
            else:
                raise NoContentError("There is no item!")
        execpt Exception as e:
            return False , str(e)

    @classmethod
    def find_by_menu_item(cls,menu_item_id):
        try:
            da = OrderMenuItemDa()
            OrderMenuItem = da.find_by_menu_item(menu_item_id)
            if OrderMenuItem:
                return True, OrderMenuItem
            else:
                 raise NoContentError("There is no item!")
        execpt  Exception as e:
            return False, str(e)

    @classmethod

    def find_by_food_order_id(cls,food_order_id ):
        try:
            da = OrderMenuItemDa()
            OrderMenuItem = da.find_by_food_order_id(food_order_id)
            if OrderMenuItem:
                return True, OrderMenuItem
            else:
                raise NoContentError("There is no food order!")
        except Exception as e:
            return False, str(e)