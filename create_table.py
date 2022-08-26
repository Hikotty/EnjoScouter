import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('sqlite:///Enjyo.db', echo=True)
Base = declarative_base()

class Enjyo(Base):
    id = Column(Integer, primary_key=True)
    word = Column(String(length=255))
    power = Column(Integer,default = 0)
    __tablename__ = 'enjyo'

Base.metadata.create_all(bind=engine)
session = sessionmaker(bind=engine)()

