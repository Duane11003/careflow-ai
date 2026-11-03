import type { Patient } from "../types/patients"

export interface PatientsListProps {
    patients: Patient[]
}

export const PatientList = ({ patients }: PatientsListProps) => {
    return patients.map((patient) => {
        return (
        <div key={patient.id}>
            <h2>{`${patient.first_name} ${patient.last_name}`}</h2>
            <p>Discharge date:{patient.discharge_date}</p>
            <p>Follow up status:{patient.follow_up_status}</p>
        </div>
        )
  })
}