from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote_plus

username = 'postgres'
password = "Exercise@2022"
host = 'localhost'
db = "postgres"
DATABASE_URL = "postgresql://postgres:%s@localhost:5432/postgres" % quote_plus("Exercise@2022")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
