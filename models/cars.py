from config.db import Base
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String



class Car(Base):
    __tablename__ = 'cars'

    registration_no = Column(String, primary_key=True)
    car_name = Column(String, nullable=False)
    model = Column(String, nullable=False)
    price = Column(Integer,nullable=False)