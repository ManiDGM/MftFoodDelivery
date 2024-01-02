#import DatabaseManager

from model.da.database import DataBaseManager
from model.entity.customer import Customer
from model.entity.food_order import Food
from model.entity.order_menu_item import Order
da=DatabaseManager()

customer=Customer(1,"ali","alipour",gender=True,email="roudgarmobina@gmail.com",password="75ff")
da.save(customer)

order=Order(1,1,1,10)
da.save(order)

food=Food(1,1,True,'2014/01/02',1000000)
da.save(food)