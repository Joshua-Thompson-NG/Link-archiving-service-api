from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

sqlite_filename = "snapshot.db"
sqlite_url = f"sqlite:///{sqlite_filename}"

engine = create_engine(sqlite_url, echo=True, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

class Base(DeclarativeBase):
    pass