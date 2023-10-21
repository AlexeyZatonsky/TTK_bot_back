from sqlalchemy import Column, Table, MetaData, String, ForeignKey, UUID, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base


metadata = MetaData()
Base = declarative_base()


class Food(Base):
    __tablename__ = 'foods'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    cost = Column(String)
    imaga_path = Column(String) 
    