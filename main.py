# para rodar o código, use o comando: uvicorn main:app --reload

from fastapi import FastAPI
from database import engine, Base
from routes.auth import auth_router
from routes.order import order_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="OrderFlow API",
    description="API para gerenciamento de pedidos",
    version="1.0.0"
)

# Inclui as rotas
app.include_router(auth_router)
app.include_router(order_router)

# Rota raiz (opcional - só para testar se a API está no ar)
@app.get("/")
def root():
    return {
        "message": "OrderFlow API está funcionando!",
        "docs": "/docs"
    }