import type { Patient } from "../types/patients"

export interface PatientDetailsProps {
    patient: Patient
}

export const PatientDetails = ({patient}: PatientDetailsProps) => {
    const {first_name, last_name, discharge_date, id, follow_up_status} = patient
    return (
        <div>
            <p>Patient Name: {`${first_name} ${last_name}`}</p>
            <p>Patient ID: {id}</p>
            <p>Discharge Date: {discharge_date}</p>
            <p>Follow Up Status: {follow_up_status}</p>
        </div>
    )

}