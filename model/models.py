from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pedidos(Base):
    __tablename__ = 'pedidos'
    id = Column(Integer, primary_key=True)
    brand = Column(String(255))
    size = Column(Integer)
    destination = Column(Text)
    color = Column(String(255))