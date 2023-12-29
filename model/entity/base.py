import sqlalchemy.orm
from sqlalchemy.orm import DeclarativeBase
# Base = declarative_base()
import json


class Base1(DeclarativeBase):
    pass
class Base(DeclarativeBase):
    def json(self):
        return json.dumps({c.name: getattr(self, c.name) for c in self.__table__.columns})
