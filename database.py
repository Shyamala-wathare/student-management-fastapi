from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Hardcoded MySQL connection string
# Change username, password, host, and database as needed
DATABASE_URL = "mysql+pymysql://root:root@localhost/db1"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()