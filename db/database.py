from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

from db.base import DatabaseConfig
from models.student_performance import Base

#create engine
print(DatabaseConfig.host)

engine = create_engine(
    f"postgresql://{DatabaseConfig.user}:{DatabaseConfig.password}@{DatabaseConfig.host}:{DatabaseConfig.port}/{DatabaseConfig.database}",
    pool_size=10,
    pool_recycle=3600,
)

# Base.metadata will collection of all tables and models
Base.metadata.bind = engine

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_session() -> Generator[Session, None, None]:
    """Create a new database session."""
    db_session = session()
    try:
        yield db_session
    finally:
        db_session.close()