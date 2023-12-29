from model.da.database import DatabaseManager
from model.entity.customer import Customer

da=DatabaseManager()

customer=Customer(1,"ali","alipour")
da.save(customer)