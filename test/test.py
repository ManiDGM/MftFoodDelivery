from model.da.database import DatabaseManager
from model.entity.customer import Customer
from model.entity.order_menu_item import Order
da=DatabaseManager()

customer=Customer(1,"ali","alipour",gender=True,email="roudgarmobina@gmail.com",password="75ff")
da.save(customer)

order=Order(1,1,1,10)
da.save(order)
