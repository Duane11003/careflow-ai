from pydantic import BaseModel, ConfigDict


class Medication(BaseModel):
    id: int
    patient_id: int
    name: str
    dosage: str
    frequency: str

    model_config = ConfigDict(from_attributes=True)