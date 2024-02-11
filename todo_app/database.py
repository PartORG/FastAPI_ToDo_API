from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:test1234@localhost:5432/TodoAppDatabase'

# check_same_thread=False -> do not check same thread, for multithreading
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# each sessionLocal will have an instance of database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# object of the database
Base = declarative_base()
