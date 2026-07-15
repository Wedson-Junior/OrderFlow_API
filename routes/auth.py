from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.users import Users
from database import get_db
from main import bcrypt_context

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get('/')
async def home():
    return {'message':'Você está na home do auth'}

@auth_router.post('/create_account')
async def create_account(email:str, password:str, username:str, session: Session = Depends(get_db)):
    user = session.query(Users).filter(Users.email==email).first()
    if user:
        return {'message':'Faild registered user'}
    else:
        encrypted_password = bcrypt_context.hash(password)
        new_user = Users(username=username, email=email, password=encrypted_password)
        session.add(new_user)
        session.commit()
        return {'message':'Successfully registered user'}