import { useSelector } from 'react-redux'
import { useAllDepartmentsQuery } from '../api/departmentApiSllice'
import { DepartmentCard, DepartmentCardSkeleton } from '../components/DepartmentCard'
import { selectCurrentUser } from '@/features/auth/store/authSlice'
import { Link } from 'react-router-dom'
import { Button } from '@/shadcnui/ui/button'

export default function ListDepartments() {
  const user = useSelector(selectCurrentUser)
  const { data, isLoading } = useAllDepartmentsQuery()
  if (isLoading) {
    return <div>Loading...</div>
  }
  let content = null
  if (isLoading) {
    content = (
      <div className='grid-cols-3 grid gap-x-4'>
        {Array.from(Array(10).keys()).map((i) => (
          <DepartmentCardSkeleton key={i} />
        ))}
      </div>
    )
  } else if (data?.length === 0) {
    content = <div className='m-auto mt-16 text-3xl text-gray-500'>No Departments Yet...</div>
  } else {
    content = (
      <div className='grid-cols-3 grid gap-x-4'>
        {data?.map((d) => (
          <DepartmentCard
            department={d}
            showUpdateButton={user != null && user.role === 'ADMIN'}
            key={d.code}
          />
        ))}
      </div>
    )
  }
  return (
    <div className='flex flex-col justify-center m-14 mx-24 space-y-4'>
      <div className='flex justify-between'>
        <p className='text-2xl'>Departments</p>
        {user != null && user.role === 'ADMIN' && (
          <Link to='/departments/create'>
            <Button variant='default'>New Department</Button>
          </Link>
        )}
      </div>
      {content}
    </div>
  )
}
