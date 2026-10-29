import { useState, useEffect } from 'react'
import type { Patient } from './types/patients'

import { getPatients } from './api/patients'

function App() {
  const [patients, setPatients] = useState<Patient[]>([])
  const [error, setError] = useState<boolean>(false)
  const [loading, setLoading] = useState<boolean>(true)

  useEffect(() => {
      const callPatients = async () => {
        try {
          const patients = await getPatients()
          setPatients(patients)
       
          
        } catch (error) {
          setError(true)
          console.error(error)
        
        } finally {
          setLoading(false)
        }
      }

      callPatients()
  }, [])

  const patientsList = patients.map((patient) => {
    return (
      <div key={patient.id}>
        <h2>{`${patient.first_name} ${patient.last_name}`}</h2>
        <p>Discharge date:{patient.discharge_date}</p>
        <p>Follow up status:{patient.follow_up_status}</p>
      </div>
    )
  })

  const errorMsg = error && <>Error fetching patients</>

  if (error) return errorMsg
  if (loading) return <p>Loading...</p>

  return (
    <>
      <section id="center">
        <div>
          {patientsList}
        </div>
      </section>

      <div className="ticks"></div>
      <section id="spacer"></section>
    </>
  )
}

export default App
