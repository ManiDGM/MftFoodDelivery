from controller import *
from model.entity import *
from model.da import *


class FoodOrderController:
    @classmethod
    def save(cls, id, customer_id, total_amount):
        try:
            da = FoodorderDa()
            if not da.find_by_customer_id(customer_id):
                foodorder = FoodorderDa(id, customer_id, total_amount)
                da.save(foodorder)
                return True, foodorder
            else:
                raise DuplicateCustomerError("Duplicate customer")

        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = FoodorderDa()
            foodorder = da.find_by_id(FoodorderDa, id)
            return True, da.remove(foodorder)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = FoodorderDa()
            return True, da.find_all(FoodorderDa)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = FoodorderDa()
            foodorder = da.find_by_id(FoodorderDa, id)
            if FoodorderDa:
                return True, foodorder
            else:
                raise NoContentError("There is no order!")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_customer_id(cls, customer_id):
        try:
            da = FoodorderDa()
            return True, da.find_by_customer_id(customer_id)
        except Exception as e:
            return False, str(e)
