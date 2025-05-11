from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from core.db.base import AbstractDatabase
import threading


#Sqlalchemy base class

class SingletonMeta(AbstractDatabase):
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "engine"):  # Avoid reinitializing
            self._setup()

    def _setup(self):
        self.engine = create_async_engine(
            "postgresql+asyncpg://postgres:postgres@localhost:5432/student-performance",
            echo=True,
        )
        self.SessionLocal = sessionmaker(
            bind=self.engine, class_=AsyncSession, expire_on_commit=False
        )

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.SessionLocal() as session:
            yield session