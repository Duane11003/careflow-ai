from datetime import date
from typing import TYPE_CHECKING

from app.database import Base
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models.patient import Patient

class Appointment(Base):
    __tablename__ = "appointments"
    id: Mapped[int] = mapped_column(primary_key=True)
    patient_id: Mapped[int] = mapped_column(ForeignKey("patients.id"))
    date: Mapped[date]
    provider: Mapped[str] = mapped_column(String(100))
    reason: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(20))
    patient: Mapped["Patient"] = relationship(back_populates="appointments")

