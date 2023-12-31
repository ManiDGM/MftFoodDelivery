from controller import *
from model.da import *
from model.entity import *
from model.entity.customer import  Customer






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
           Customer.id=id
           da.edit(Customer)
           return True,Customer
       except Exception as e:
           e.with_traceback()
           return False, str(e)

    @classmethod
    def remove(cls,id):
        try:
            da = CustomerDa()
            Customer = da.find_by_id(Customer,id)
            return True, da.remove(Customer)
        except Exception as e:
            return False,str(e)

    @classmethod
    def find_all(cls):
        try:
            da = CustomerDa()
            return True,da.find_all(Customer)
        except Exception as e:
            return False,str(e)

    @classmethod
    def find_by_id(cls,id):
        try:
            da = CustomerDa()
            Customer = da.find_by_id(Customer,id)
            if Customer:
                return True,Customer
            else:
                raise NoContentError("There is no Customer!")
        execpt Exception as e: 
            return False , str(e)


    @classmethod
    def find_by_email(cls, email):
        try:
            da = CustomerDa()
            return True,da.find_by_email(email)
        except Exception as e:
            return False,str(e)

    @classmethod
    def login(cls,email,password):
        try:
            da = CustomerDa()
            Customer = da.find_by_email_password(email,password)
            if (Customer):
                return True,Customer
            else:
                raise AccessDeniedError("wrong email/password")
        except Exception as e:
            return  False,str(e)
