from datetime import datetime

from controller import CustomerController
from model.da.database import *
from model.entity import *

# da = DataBaseManager()
# customer = da.find_by_id(Customer, 10)
# # da.save(customer)
#
#
# order = FoodOrder(customer, True, datetime.now(), 1000)
# da.save(order)
#
# menuitem=Menu("peperoni",12346)
# da.save(menuitem)
#
# order_menu_item=OrderMenuIte',m(order,menuitem,10)
# da.save(order_menu_ite'ahmadm)'
CustomerController.save("ahmad","messbah","A@A.com","A123")
CustomerController.save("ahmad","messbah","A@A.com","A123")



# CustomerController.save("ahmad","messbah","A@A.com","A123")
# CustomerController.edit(11,"ahmadaaaa","messbah","A@A.com","A123")
CustomerController.remove(11)