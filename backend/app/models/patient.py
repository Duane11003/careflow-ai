from datetime import date
from typing import TYPE_CHECKING

from app.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models.appointment import Appointment
    from app.models.medication import Medication

class Patient(Base):
    __tablename__ = "patients"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    discharge_date: Mapped[date]
    follow_up_status: Mapped[str] = mapped_column(String(20))
    medications: Mapped[list["Medication"]] = relationship(back_populates="patient")
    appointments: Mapped[list["Appointment"]] = relationship(back_populates="patient")