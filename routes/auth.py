from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.users import Users
from database import get_db
from main import bcrypt_context
from schemas.users import Users_schemas, Login_schemas

auth_router = APIRouter(prefix="/auth", tags=["auth"])

def autenticate_user(email:str, password:str, session: Session):
    user = session.query(Users).filter(Users.email==email).first()
    if not user:
        return False
    elif not bcrypt_context.verify(password, user.password):
        return False
    return user


@auth_router.get('/')
async def home():
    return {'message':'You are at the auth home'}

@auth_router.post('/create_account')
async def create_account(userschema: Users_schemas, session: Session = Depends(get_db)):
    user = session.query(Users).filter(Users.email==userschema.email).first()
    if user:
        raise HTTPException(status_code=400, detail='Faild registered user')
    else:
        encrypted_password = bcrypt_context.hash(userschema.password)
        new_user = Users(
            username=userschema.name, 
            email=userschema.email, 
            password=encrypted_password,
            active=userschema.active,
            admin=userschema.admin
            )
        session.add(new_user)
        session.commit()
        return {'message':'Successfully registered user'}

@auth_router.post('/login')
async def login(loginschema:Login_schemas , session: Session = Depends(get_db)):
    user = autenticate_user(
        email    =loginschema.email, 
        password =loginschema.password, 
        session  =session
        )
    if not user:
        raise HTTPException(status_code=400, detail='Failed to authenticate email or password')
    else:
        return {'message':'You logged'}