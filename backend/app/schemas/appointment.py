from datetime import date

from pydantic import BaseModel, ConfigDict

class Appointment(BaseModel):
    id: int
    patient_id: int
    date: date
    provider: str
    reason: str
    status: str

    model_config = ConfigDict(from_attributes=True)