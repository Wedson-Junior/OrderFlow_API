import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from sqlalchemy.engine import URL

from alembic import context

# ================== CONFIGURAÇÃO DO PROJETO ==================
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Importa todos os models
from models.base import Base
from models.users import Users
from models.items import Items
from models.orders import Orders
from models.order_items import OrderItems

# ============================================================

config = context.config

# Força a leitura da URL do alembic.ini
if not config.get_main_option("sqlalchemy.url"):
    config.set_main_option("sqlalchemy.url", "sqlite:///data/orderflow.db")

target_metadata = Base.metadata

def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    configuration = config.get_section(config.config_ini_section) or {}
    url = configuration.get("sqlalchemy.url") or config.get_main_option("sqlalchemy.url")
    
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
        url=url,                   
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()