import { useGetPatientsQuery } from './api/patientsApi'
import { PatientList } from './components/PatientList'
import { DropdownFilter } from './components/DropdownFilter'
import { useState } from 'react'
import type { StatusFilter } from './types/filter'

function App() {
  const { data: patients, isLoading, isError } = useGetPatientsQuery()
  const [statusFilter, setStatusFilter] = useState<StatusFilter>('All')

const filteredPatients = (patients ?? []).filter(
  (patient) =>
    statusFilter === 'All' ||
    patient.follow_up_status === statusFilter
)


  if (isError) return <p>Error fetching patients</p>
  if (isLoading) return <p>Loading...</p>

  return (
    <>
      <section id="center">
        <div>
          <DropdownFilter onChange={setStatusFilter} />
          <PatientList patients={filteredPatients} />
        </div>
      </section>

      <div className="ticks"></div>
      <section id="spacer"></section>
    </>
  )
}

export default App
