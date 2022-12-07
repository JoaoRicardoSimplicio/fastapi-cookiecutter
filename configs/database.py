import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL_FORMAT = "postgresql://{user}:{password}@{host}/{database}"
SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL_FORMAT.format(
    user=os.environ.get("POSTGRES_USER"),
    password=os.environ.get("POSTGRES_PASSWORD"),
    host=os.environ.get("POSTGRES_HOST"),
    database=os.environ.get("POSTGRES_DB")
)


engine = sessionmaker(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocomit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
