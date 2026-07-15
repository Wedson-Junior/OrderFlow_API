# para rodar o código, use o comando: uvicorn main:app --reload

from fastapi import FastAPI
from database import engine, Base
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

Base.metadata.create_all(bind=engine)

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto', bcrypt__rounds=12,bcrypt__truncate_error=False)

app = FastAPI(
    title="OrderFlow API",
    description="API para gerenciamento de pedidos",
    version="1.0.0"
)

# Inclui as rotas
from routes.auth import auth_router
from routes.order import order_router

app.include_router(auth_router)
app.include_router(order_router)

# Rota raiz (opcional - só para testar se a API está no ar)
@app.get("/")
def root():
    return {
        "message": "OrderFlow API está funcionando!",
        "docs": "/docs"
    }