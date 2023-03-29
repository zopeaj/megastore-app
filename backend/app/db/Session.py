from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



# Connecting
from sqlalchemy import create_engine

SQLITE_DB_URL = "sqlite:///./test.db"

engine = create_engine(SQLITE_DB_URL, echo=True, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


