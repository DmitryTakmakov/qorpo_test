import datetime

from pydantic import BaseModel, ConfigDict, field_serializer


class CurrencyModel(BaseModel):
    id: int
    currency: str
    date_: datetime.datetime
    price: float

    model_config = ConfigDict(from_attributes=True)

    @field_serializer("date_")
    def serialize_date(self, date: datetime.datetime):
        return str(date.replace(microsecond=0))

    @field_serializer("price")
    def serialize_price(self, price: float):
        return round(price, 2)


__all__ = ["CurrencyModel"]
