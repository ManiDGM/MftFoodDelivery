from datetime import datetime
from controller import *
from model.da import FoodOrderDa
from model.da.database import *
from model.entity import *


#da = DataBaseManager()
# customer = da.find_by_id(Customer, 12)
# da.save(customer)
#
##
# order = FoodOrder(customer, True, datetime.now(), 1000)
# da.save(order)
#
# menuitem=Menu("peperoni",12346)
# da.save(menuitem)
#
# order_menu_item=OrderMenuIte',m(order,menuitem,10)
# da.save(order_menu_ite'ahmadm)'
# CustomerController.save("ahmad","messbah","A@A.com","A123")
#CustomerController.save("mobinaaaa","rou","A@Ad.com","A12dd3")


# print( CustomerController.save("ahmad","messbah","A@A.com","A123"))
# CustomerController.edit(11,"ahmadaaaa","messbah","A@A.com","A123")
# CustomerController.remove()
# CustomerController.find_all()
# print(CustomerController.find_by_id(12))
# print(CustomerController.find_by_email("A@A.com"))
# print(CustomerController.login("A@A.com","A1238"))

#print(FoodOrderController.save(17, True, datetime.now(), 158.55528))
#FoodOrderController.edit(9,16,True,datetime.now(),120055)
#FoodOrderController.remove(9)
#print(FoodOrderController.find_all())
#print(FoodOrderController.find_by_id(7))
#print(FoodOrderController.find_by_customer_id(15))


# MenuController.save("bergurww",100000)
# MenuController.edit(8,"bergur111",2222)
# MenuController.remove(8)
# MenuController.find_all()
# MenuController.find_by_id(10)
# ??????????MenuController.find_by_order_menu()

# MenuController.find_by_item_name("bergurww")
#da=FoodOrderDa()
#foodorder = FoodOrder(15, True, datetime.now(), 2)
#da.save(foodorder)

print(OrderMenuItemController.save(7,10,10))
