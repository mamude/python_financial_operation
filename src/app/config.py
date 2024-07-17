import os

from pydantic import BaseModel, PostgresDsn


class Settings(BaseModel):
    pg_dsn: PostgresDsn = os.getenv("DATABASE_URL")