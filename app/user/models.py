from sqlalchemy import String, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from app.extensions import db

class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_namae: Mapped[str] = mapped_column(String(20))
    last_namae: Mapped[str] = mapped_column(String(20))
    age: Mapped[int] = mapped_column(SmallInteger)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    address: Mapped[str] = mapped_column(SmallInteger)


