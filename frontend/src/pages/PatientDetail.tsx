import { useParams, Link } from "react-router"
import { useGetPatientsByIdQuery } from "../api/patientsApi"
import { skipToken } from '@reduxjs/toolkit/query'
import { PatientDetails } from "../components/PatientDetails"

export const PatientDetail = () => {

    const { id } = useParams()
    const numberId = Number(id)
    const isValidParameter = Number.isInteger(numberId) && numberId > 0
    const { data: patient, isLoading, isError } = useGetPatientsByIdQuery(isValidParameter ? numberId : skipToken)

    if (isLoading) return <p>Loading patient data...</p>
    if (isError) return <p>Failed to load data</p>
    if (!isValidParameter) return <p>Invalid patient ID</p>
    if (!patient) return <p>Patient not found</p>
    
    return (
        <div>
            <PatientDetails patient={patient}  />
            <Link to="/">Back to Dashboard</Link>
        </div>
    )
}