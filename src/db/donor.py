from sqlalchemy import BigInteger
from sqlalchemy import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Donor(Base):
    """QuizUser model."""

    __tablename__ = 'accounts'


    user_id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, unique=True, nullable=False
    )
    fio: Mapped[str] = mapped_column(
        VARCHAR(255), unique=False, nullable=True
    )
    group: Mapped[str] = mapped_column(
        E, unique=False, nullable=True
    )
    gavrilov_amount: Mapped[int] = mapped_column(
        Inte, unique=False, nullable=True
    )
    fmba_amount: Mapped[int] = mapped_column(
        E, unique=False, nullable=True
    )
