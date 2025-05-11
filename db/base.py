from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator


class AbstractDatabase(ABC):
    @abstractmethod
    def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """Get a database session."""
        pass

