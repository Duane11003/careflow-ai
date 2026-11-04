import type { Patient } from '../types/patients'

interface PatientListProps {
  patients: Patient[]
}

export const PatientList = ({ patients }: PatientListProps) => {
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
            <td>{`${patient.first_name} ${patient.last_name}`}</td>
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