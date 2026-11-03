import { type Patient } from '../types/patients'

export const getPatients = async (): Promise<Patient[]> => {
    const response = await fetch('/api/patients');
    if (!response.ok) {
        throw new Error('Failed to fetch patients');
    }
    return response.json();
}