from pydantic import BaseModel
from typing import Optional

class Users_schemas(BaseModel):
    name      : str
    email     : str
    password  : str
    active    : Optional[bool]
    admin     : Optional[bool] = False

    class Config:
        from_attributes = True

class Login_schemas(BaseModel):
    email     : str
    password  : str

    class Config:
        from_attributes = True