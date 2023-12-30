from controller import *
from model.da import *
from model.entity import *
from model.entity.customer import Customer


class DuplicateemailError:
    pass


class CustomerDa:
    pass


class CustomerController:
    @classmethod
    def save(cls,name,family,email,password):
        try:
            da = CustomerDa()
            if not da.find_by_email(email):
                profile = Customer(name, family, email, password)
                da.save(Customer)
                return True, Customer
            else:
                raise DuplicateemailError ("Duplicate email")
        except Exception as e:
            return False, str(e)
    @classmethod
    def edit(cls, id, name, family, email, password, username=None):
       try:
       da = CustomerDa()
       Customer = Customer(name,family,username,password)

