from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlmodel import  Session, SQLModel
# from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./data/tickets.db"
engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

def create_db_table():
    SQLModel.metadata.create_all(bind=engine)

def get_session():
    with Session(bind=engine) as session:
        yield session

sessionDepends = Annotated[Session, Depends(get_session)]