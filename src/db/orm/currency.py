from typing import Optional

from sqlalchemy import select
from src.db.models import Currency
from src.db.orm.base import BaseDAO
from src.db.schemas import CurrencyModel


class CurrencyDAO(BaseDAO):
    model_class = Currency

    async def list(self, offset: int, limit: int = 10) -> list[Optional[dict]]:
        query = select(self.model_class).order_by(self.model_class.date_.desc()).limit(limit)
        if offset != 1:
            query = query.offset(offset)
        result = await self.session.scalars(query)
        return [CurrencyModel.model_validate(_).model_dump() for _ in result]


__all__ = ["CurrencyDAO"]
