from datetime import datetime
from typing import Optional, List

from sqlalchemy import Integer, String, func
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.core.entities import Base
from app.core.entities.product import Product


class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str]
    fullname: Mapped[Optional[str]]
    nickname: Mapped[Optional[str]] = mapped_column(String(64))
    create_date: Mapped[datetime] = mapped_column(insert_default=func.now())

    products: Mapped[List["Product"]] = relationship(back_populates="user")
