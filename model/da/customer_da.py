from sqlalchemy import and_

from model.da.database import DataBaseManager ,and_
from model.entity.customer import Customer


class CustomerDa(DataBaseManager):
    def find_by_email_password(self,email,password):
        self.make_engine()
        result=self.session.query(Customer).filter(and_(Customer.email==email,Customer.password==password))
        self.session.close()
        return  result

    def find_by_email(self,email):
        self.make_engine()
        result= self.session.query(Customer).filter(Customer.email==email)
        try :
            if (result.email):
                self.session.close()
                return result
        except:
            return None

