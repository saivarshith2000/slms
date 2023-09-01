import { Button } from '@/shadcnui/ui/button'
import { Department } from '../types'
import { Skeleton } from '@/shadcnui/ui/skeleton'
import { useNavigate, createSearchParams } from 'react-router-dom'

type DepartmentCardPropType = {
  department: Department
  showUpdateButton: boolean
}

export function DepartmentCard({ department, showUpdateButton }: DepartmentCardPropType) {
  const navigate = useNavigate()

  function handleOnClick() {
    navigate({ pathname: '/departments/update', search: createSearchParams(department).toString() })
  }

  return (
    <div className='flex flex-col items-start space-y-1 border-2 p-4 b-2 bg-white rounded-md'>
      <h2 className='text-xl font-semibold'>{department.name}</h2>
      <h2>{department.code}</h2>
      <p className='text-gray-400 truncate w-[250px]'>{department.description}</p>
      {showUpdateButton && (
        <Button variant='outline' size='sm' onClick={handleOnClick}>
          Update
        </Button>
      )}
    </div>
  )
}

export function DepartmentCardSkeleton() {
  return (
    <div className='flex flex-col items-start space-y-4 border-2 p-4 mb-2 bg-white rounded-md'>
      <Skeleton className='h-4 w-[250px]' />
      <Skeleton className='h-4 w-[200px]' />
    </div>
  )
}
