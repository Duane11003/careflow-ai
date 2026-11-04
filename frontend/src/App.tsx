import { Routes, Route } from 'react-router'
import PatientDashboard from './pages/PatientDashboard'
import { PatientDetail } from './pages/PatientDetail'

function App() {
  return (
    <Routes>
      <Route path="/" element={<PatientDashboard />} />
      <Route path="/patients/:id" element={<PatientDetail />} />
    </Routes>
  )
}

export default App