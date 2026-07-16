from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy_utils import ChoiceType
from .base import Base

class Items(Base):
    __tablename__ = 'items'

    ITEMS_CATEGORY = (
        ('SWEET', 'SWEET'),
        ('SALTY', 'SALTY')
        )

    id = Column(Integer, autoincrement=True, primary_key=True)
    item_description = Column(String)
    category = Column(String, ChoiceType(ITEMS_CATEGORY))
    active = Column(Boolean, default=True)

    def __init__(self, item_description, active, category):
        self.item_description = item_description
        self.category = category
        self.active = active