import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context
from sqlalchemy import pool
from logging.config import fileConfig
from config import setting
from app.database import Base
from app.models.User import User  # make sure this imports your models

# Alembic Config object
config = context.config
config.set_main_option("sqlalchemy.url", setting.DATABASE_URL)

# Logging setup
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata for autogenerate
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = setting.DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    """Synchronous function called by run_sync to run migrations."""
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode using async engine."""
    connectable = create_async_engine(setting.DATABASE_URL, poolclass=pool.NullPool)

    async with connectable.connect() as connection:
        # run_sync wraps your synchronous migration function
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())