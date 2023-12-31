class FoodOrderController:
    @classmethod
    def save (cls,id,customer_id,total_amount)
        try:
            da = FoodOrder()
            if not da.find_by_customer_id(customer_id)
               FoodOrder =FoodOrder(id,customer_id,total_amount)
               da.save(FoodOrder)
               return True,FoodOrder
             else:
                  raise DuplicatecustomeridError("Duplicate customer")

        except Exception as e:
            return False,str(e)
    @classmethod
    def remove(cls,id):
        try:
            da = FoodOrderDa()
            FoodOrder = da.find_by_id(FoodOrder,id)
            return True,da.remove(FoodOrder)
        except Exception as e:
            return False,str(e)

    @classmethod
    def find_all(cls):
        try:
            da = FoodOrderDa()
            return True,da.find_all(FoodOrder)
        except Exception as e:
            return False,str(e)

    @classmethod
    def find_by_id(cls,id):
        da = FoodOrderDa()
        FoodOrder = da.find_by_id(FoodOrder,id)
        if FoodOrder:
            return True,FoodOrder
        else:
            raise NoContentError("There is no order!")
        except Exception as e:
             return False,str(e)

    @classmethod
    def find_by_customer_id(cls,customer_id):
        try:
            da = FoodOrderDa()
            return True,da.find_by_customer_id(customer_id)
        except Exception as e:
            return False,str(e)

