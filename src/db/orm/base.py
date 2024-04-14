from typing import Any, Optional, Type, TypeVar

from sqlalchemy import Column, delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.models import Base

T = TypeVar("T", bound=Base)


class BaseDAO:
    model_class: Type[T] = None

    def __init__(self, db_session: AsyncSession):
        if self.model_class is None:
            raise NotImplementedError
        self.session = db_session

    async def create(self, **kwargs) -> T:
        _obj = self.model_class(**kwargs)
        self.session.add(_obj)
        await self.session.commit()
        return _obj

    async def get_by_column(self, column: Column, value: Any) -> Optional[T]:
        query = select(self.model_class).where(column == value)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def flush_table(self) -> None:
        await self.session.execute(delete(self.model_class))
        await self.session.commit()


__all__ = ["BaseDAO"]
