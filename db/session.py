from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

from core.config import settings


# Import all models BEFORE engine creation
from db.models.user import User
from db.models.blog import Blog


#SQL alchemy orm which connects to the postgressql 
SQLALCHEMY_DATABSE_URL = settings.DATABASE_URL
print(SQLALCHEMY_DATABSE_URL)
engine = create_engine(SQLALCHEMY_DATABSE_URL)



# for the sqlite connection.
# check_same_thread used beca sqlite db handle only single thread.
# SQLALCHEMY_DATABSE_URL = "sqlite:///./sql_app.db"
# engine = create_engine(SQLALCHEMY_DATABSE_URL, connect_args={"check_same_thread":False} )

SESSIONLOCAL = sessionmaker(autoflush=False , autocommit=False , bind=engine)

def get_db() -> Generator:
    try:
        db = SESSIONLOCAL()
        yield db
    finally:
        db.close()

