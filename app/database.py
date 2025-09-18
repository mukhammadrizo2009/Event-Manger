from sqlalchemy import (
    create_engine, 
    URL
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from . import config

Database_URL = URL.create(
    drivername="postgresql+psycopg2",
    host=config.DB_HOST,
    port=config.DB_PORT,
    username=config.DB_USER,
    password=config.DB_PASSWORD,
    database=config.DB_NAME
)

engine = create_engine(Database_URL)
Base = declarative_base()
LocalSession = sessionmaker(autocommit=False , autoflush=True , bind=engine)

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()