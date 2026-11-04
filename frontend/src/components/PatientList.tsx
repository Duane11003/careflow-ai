import type { Patient } from '../types/patients'

interface PatientListProps {
  patients: Patient[]
  onSelectPatient: (patientId: number) => void
}

export const PatientList = ({ patients, onSelectPatient }: PatientListProps) => {
  return (
    <table>
      <thead>
        <tr>
          <th>Patient ID</th>
          <th>Name</th>
          <th>Discharge Date</th>
          <th>Follow-up Status</th>
        </tr>
      </thead>

      <tbody>
        {patients.map((patient) => (
          <tr key={patient.id}>
            <td>{patient.id}</td>
            <td>
              <button type='button' onClick={() => onSelectPatient(patient.id)}>
                {`${patient.first_name} ${patient.last_name}`}
              </button>
            </td>
            <td>{patient.discharge_date}</td>
            <td>
              {patient.follow_up_status.charAt(0).toUpperCase() +
                patient.follow_up_status.slice(1)}
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  )
}