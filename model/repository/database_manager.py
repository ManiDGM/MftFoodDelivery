from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.entity.base import Base


class DatabaseManager:
    def __init__(self):
        self.session = None
        self.engine = None

    def make_engine(self):
        if not self.engine:
            self.engine = create_engine("mysql+pymysql://root:root123@localhost:3306/MftFoodDelivery")
            # self.engine = create_engine('oracle://python:python123@localhost:1521/xe', echo='debug')
            # id_seq = Sequence('PERSONS_SEQ', metadata=Base.metadata)
            # id = Column('ID', String(20), id_seq, primary_key=True)
            Base.metadata.create_all(self.engine)
            Session = sessionmaker(bind=self.engine)
            self.session = Session()


