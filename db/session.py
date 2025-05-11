from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from core.db.base import AbstractDatabase
import threading


#Sqlalchemy base class

class SingletonMeta(AbstractDatabase):
    """
    Singleton metaclass to ensure a single instance of the database session.
    This class is thread-safe and ensures that only one instance of the database
    session is created, even in a multi-threaded environment.

    """
    # Singleton instance
    _instance = None
    # Lock for thread-safe singleton instance creation
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        """"
        Create a new instance of the SingletonMeta class.
        """
        # Check if an instance already exists
        if not cls._instance:
            # If not, acquire the lock and create a new instance
            with cls._lock:
                # Double-check if an instance was created while waiting for the lock
                if not cls._instance:
                    # Create a new instance of the class
                    cls._instance = super().__new__(cls)
        return cls._instance

    
    def _setup(self):
        """
        Set up the database engine and sessionmaker.
        This method is called when the instance is created to initialize the
        """
        # Create the database engine
        # using the asyncpg driver for PostgreSQL
        self.engine = create_async_engine(
            "postgresql+asyncpg://postgres:postgres@localhost:5432/student-performance",
            echo=True,
        )
        # Create the sessionmaker
        # using the AsyncSession class for asynchronous database operations
        self.SessionLocal = sessionmaker(
            bind=self.engine, class_=AsyncSession, expire_on_commit=False
        )

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """	
        Get a database session.
        This method returns an asynchronous generator that yields a session
        """
        async with self._sessionmaker() as session:
            yield session


