from datetime import date
from sqlalchemy import Date
from sqlalchemy import Integer
from sqlalchemy import Enum
from sqlalchemy import VARCHAR, CHAR
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Donor(Base):
    """Donor model."""

    __tablename__ = 'donors'


    fio: Mapped[str] = mapped_column(
        VARCHAR(255), unique=False, nullable=True
    )
    group: Mapped[str] = mapped_column(
        VARCHAR(9), unique=False, nullable=True
    )
    gavrilov_amount: Mapped[int] = mapped_column(
        Integer, unique=False, nullable=True
    )
    fmba_amount: Mapped[int] = mapped_column(
        Integer, unique=False, nullable=True
    )
    sum: Mapped[int] = mapped_column(
        Integer, unique=False, nullable=True
    )
    gavrilov_last_donation_date: Mapped[date] = mapped_column(
        Date, unique=False, nullable=True
    )
    fmba_last_donation_date: Mapped[date] = mapped_column(
        Date, unique=False, nullable=True
    )
    social_contacts: Mapped[str] = mapped_column(
        VARCHAR(255), unique=False, nullable=True
    )
    number: Mapped[str] = mapped_column(
        CHAR(12), unique=False, nullable=True
    )
