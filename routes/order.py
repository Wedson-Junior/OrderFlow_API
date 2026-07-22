from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from schemas.orders import Orders_schemas
from models.orders import Orders

order_router = APIRouter(prefix="/orders", tags=["orders"])

@order_router.get('/')
async def order_home():
    return {'message':'you are in the order home'}

@order_router.post('/make_order')
async def make_order(orderschema : Orders_schemas, session : Session=Depends(get_db)):
    try:
        new_order = Orders(user_id=orderschema.user_id)
        session.add(new_order)
        session.commit()
    except:
        raise HTTPException(status_code=400, detail='User not found')
    return {'message': 'Order created successfully'}