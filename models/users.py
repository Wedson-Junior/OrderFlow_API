from sqlalchemy import Column, Integer, String, Boolean, Float ,ForeignKey
from .base import Base

class Users(Base):
    __tablename__ = 'users'

    id       = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    email    = Column(String, nullable=False, unique=True)
    password = Column(String)
    active   = Column(Boolean, default=True)
    admin    = Column(Boolean, default=False)

    def __init__(self, username, email, password, active=True, admin=False):
        self.username = username
        self.email    = email
        self.password = password
        self.active   = active
        self.admin    = admin

