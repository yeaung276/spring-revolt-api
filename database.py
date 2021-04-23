from dotenv import load_dotenv
from functools import lru_cache
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

@lru_cache
def cache_dotenv():
    load_dotenv()
cache_dotenv()

SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL') 


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
