from sqlalchemy import Column, Integer, String, Float ,ForeignKey
from sqlalchemy_utils import ChoiceType
from .base import Base

class Orders(Base):
    __tablename__ = 'orders'

    STATUS_ORDERS = (
        ('PENDING', 'PENDING'), 
        ('COMPLETED', 'COMPLETED'), 
        ('CANCELLED', 'CANCELLED')
    )

    id       = Column(Integer, primary_key=True, autoincrement=True)
    status   = Column(String, ChoiceType(choices=STATUS_ORDERS))
    user_id  = Column(Integer, ForeignKey('users.id'))
    price    = Column(Float)

    def __init__(self, user_id, price, status="PENDING"):
        self.status = status
        self.user_id = user_id
        self.price = price
