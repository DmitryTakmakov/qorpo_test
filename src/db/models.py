from sqlalchemy import BigInteger, Column, DateTime, Float, String, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Currency(Base):
    __tablename__ = "currencies"

    id = Column("id", BigInteger, primary_key=True, autoincrement="auto")
    currency = Column("currency", String(16), nullable=False)
    date_ = Column("date_", DateTime, server_default=func.now())
    price = Column("price", Float(precision=4), nullable=False)

    __mapper_args__ = {"eager_defaults": True}


__all__ = ["Base", "Currency"]
