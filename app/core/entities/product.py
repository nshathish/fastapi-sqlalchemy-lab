from sqlalchemy import Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.core.entities import Base
from app.core.entities.user import User


class Product(Base):
    __tablename__ = "products"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str]

    user: Mapped["User"] = relationship(back_populates="products")