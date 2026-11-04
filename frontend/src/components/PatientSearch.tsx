interface PatientSearchProps {
  value: string
  onChange: (value: string) => void
}

export const PatientSearch = ({ value, onChange }: PatientSearchProps) => {
  return (
    <input
      type="search"
      placeholder="Search patients..."
      value={value}
      onChange={(e) => onChange(e.target.value)}
    />
  )
}