import { configureStore } from "@reduxjs/toolkit";
import { patientsApi } from "../api/patientsApi";

export const store = configureStore({
    reducer: { [patientsApi.reducerPath]: patientsApi.reducer },
    middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(patientsApi.middleware)
})

export type AppStore = typeof store
export type RootState = ReturnType<AppStore['getState']>
export type AppDispatch = AppStore['dispatch']