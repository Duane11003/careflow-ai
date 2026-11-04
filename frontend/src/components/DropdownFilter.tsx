import type { StatusFilter } from "../types/filter"

export interface DropdownFilterProps {
    onChange: (value: StatusFilter) => void
}

export const DropdownFilter = ({onChange}: DropdownFilterProps) => {
    return (
        <select onChange={(e) => onChange(e.target.value as StatusFilter)}>
            <option value="All">All Patients</option>
            <option value="Pending">Pending</option>
            <option value="Completed">Completed</option>
        </select>
    )
}