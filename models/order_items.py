from sqlalchemy import Column, Integer, Float ,ForeignKey
from .base import Base

class OrderItems(Base):
    __tablename__ = 'order_items'

    id       = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    item_id  = Column(Integer, ForeignKey('items.id'))
    quantity = Column(Integer)
    price    = Column(Float)

    def __init__(self, order_id, quantity, price):
        self.order_id = order_id
        self.quantity = quantity
        self.price    = price