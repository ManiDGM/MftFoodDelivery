from model.da.database import DatabaseManager
from model.entity.customer import Customer

da=DatabaseManager()

customer=Customer(2,"ali","alipour")
da.save(customer)
