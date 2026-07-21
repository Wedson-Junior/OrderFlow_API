from pydantic import BaseModel

class Orders_schemas(BaseModel):
    user_id : int

    class Config:
        from_attributes = True