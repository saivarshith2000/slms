type RoleBadgeType = {
  role: 'ADMIN' | 'STUDENT' | 'TEACHER'
}

export default function RoleBadge({ role }: RoleBadgeType) {
  let bg = 'bg-red-500'
  if (role == 'STUDENT') bg = 'bg-blue-500'
  else if (role == 'TEACHER') bg = 'bg-orange-500'

  return (
    <span className={`text-[11px] font-bold p-0.5 px-1 text-white ${bg} rounded-md`}>{role}</span>
  )
}
