**Aqui está uma versão bem melhorada do seu README.md:**

# OrderFlow API

API para gerenciamento de pedidos e usuários, desenvolvida com **FastAPI** + **SQLAlchemy** + **PostgreSQL**.

---

## ✨ Funcionalidades

- Cadastro e login de usuários (com JWT)
- Gerenciamento de pedidos (em desenvolvimento)
- Autenticação protegida por token
- Migrações de banco com Alembic

---

## 🚀 Como rodar o projeto

### Pré-requisitos
- Python 3.10+
- PostgreSQL instalado e rodando
- (Opcional) uv ou virtualenv

### 1. Clone o repositório
```bash
git clone https://github.com/Wedson-Junior/OrderFlow_API.git
cd OrderFlow_API
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux / Mac:
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o arquivo `.env`
Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
DATABASE_URL=postgresql://usuario:senha@localhost:5432/orderflow_db
SECRET_KEY=sua_chave_secreta_muito_longa_e_segura_aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Crie o banco de dados e rode as migrações
```bash
# Crie o banco no PostgreSQL (se ainda não existir)
# Depois rode:
alembic upgrade head
```

### 6. Rode a API
```bash
uvicorn main:app --reload
```

A API estará disponível em: **http://127.0.0.1:8000**

- Documentação interativa: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Roadmap (Próximos passos)

### Fase 1 - Fundamentos (Atual)
- [x] Configuração inicial do FastAPI
- [x] Modelos de banco (User, Order, OrderItem)
- [x] Sistema básico de autenticação (JWT)
- [ ] Completar rotas de autenticação (register + login)
- [ ] Proteção das rotas com token

### Fase 2 - Funcionalidades principais
- [ ] CRUD completo de Pedidos (criar, listar, detalhar, atualizar status)
- [ ] Relacionamento entre User e Orders
- [ ] Validações fortes com Pydantic
- [ ] Filtros e paginação nos pedidos

### Fase 3 - Melhoria e Produção
- [ ] Testes automatizados (pytest)
- [ ] Docker + docker-compose
- [ ] Tratamento avançado de erros
- [ ] Rate limiting
- [ ] Documentação completa no README
- [ ] Deploy (Railway, Render ou similar)

---

## Tecnologias utilizadas

- **FastAPI** - Framework web
- **SQLAlchemy** - ORM
- **Alembic** - Migrações
- **PostgreSQL** - Banco de dados
- **JWT + bcrypt** - Autenticação
- **Pydantic** - Validação

---

**Contribuição**  
Sinta-se à vontade para abrir issues ou pull requests!

---