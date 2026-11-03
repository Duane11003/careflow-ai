import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import type { Patient } from "../types/patients";

export const patientsApi = createApi({
    reducerPath: 'patientsApi',
    baseQuery: fetchBaseQuery({ baseUrl: '/api'}),
    endpoints: (build) => ({
        getPatients: build.query<Patient[], void>({ // returnType, queryParam
            query: () => `patients`
        })
    })
})

export const { useGetPatientsQuery } = patientsApi