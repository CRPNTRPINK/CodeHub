import os

from dotenv import load_dotenv

load_dotenv()

REAL_DATABASE_URL = os.getenv(
    "REAL_DATABASE_URL",
    "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"
)
