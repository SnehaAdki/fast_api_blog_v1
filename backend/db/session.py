from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

SQLALCHEMY_DATABSE_URL = settings.DATABASE_URL
print(SQLALCHEMY_DATABSE_URL)

engine = create_engine(SQLALCHEMY_DATABSE_URL)

SESSIONLOCAL = sessionmaker(autoflush=False , autocommit=False , bind=engine)


