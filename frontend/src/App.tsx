import { useGetPatientsQuery } from './api/patientsApi'
import { PatientList } from './components/PatientList'

function App() {
  const { data: patients, isLoading, isError } = useGetPatientsQuery()


  if (isError) return <p>Error fetching patients</p>
  if (isLoading) return <p>Loading...</p>

  return (
    <>
      <section id="center">
        <div>
          <PatientList patients={patients ?? []} />
        </div>
      </section>

      <div className="ticks"></div>
      <section id="spacer"></section>
    </>
  )
}

export default App
