import { useGetPatientsQuery } from './api/patientsApi'
import { PatientList } from './components/PatientList'
import { PatientDetails } from './components/PatientDetails'
import { PatientSearch } from './components/PatientSearch'
import { DropdownFilter } from './components/DropdownFilter'
import { useState } from 'react'
import type { StatusFilter } from './types/filter'

function App() {
  const { data: patients, isLoading, isError } = useGetPatientsQuery()
  const [statusFilter, setStatusFilter] = useState<StatusFilter>('All')
  const [searchTerm, setSearchTerm] = useState<string>('')
  const [selectedPatientId, setSelectedPatientId] = useState<number | null>(null)

  const selectedPatient = patients?.find((patient) => patient.id === selectedPatientId)

  const handlePatientSearch = (term: string) => {
    setSearchTerm(term)
  }

const normalizedSearchTerm = searchTerm.trim().toLowerCase()
const filteredPatients = (patients ?? []).filter((patient) => {
   const patientFullName = `${patient.first_name} ${patient.last_name}`.toLowerCase()
    return (
    (statusFilter === 'All' || patient.follow_up_status === statusFilter) && patientFullName.includes(normalizedSearchTerm)
     )
})

const handlePatientSelect = (patientId: number) => {
  setSelectedPatientId(patientId)
}


  if (isError) return <p>Error fetching patients</p>
  if (isLoading) return <p>Loading...</p>

  return (
    <>
      <section id="center">
        <div>
          <PatientSearch value={searchTerm} onChange={handlePatientSearch} />
          <DropdownFilter onChange={setStatusFilter} />
          <PatientList onSelectPatient={handlePatientSelect} patients={filteredPatients} />
        </div>
        { selectedPatient && <PatientDetails patient={selectedPatient} />}

      </section>

      <div className="ticks"></div>
      <section id="spacer"></section>
    </>
  )
}

export default App
