from pydantic import BaseModel
from datetime import date

class Patient(BaseModel):
    id: int
    first_name: str
    last_name: str
    discharge_date: date
    follow_up_status: str

