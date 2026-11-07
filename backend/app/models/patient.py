from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from datetime import date

class Patient(Base):
    __tablename__ = "patients"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    discharge_date: Mapped[date]
    follow_up_status: Mapped[str] = mapped_column(String(20))