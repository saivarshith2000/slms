import { useAllUsersQuery } from '../api/adminApiSlice'
import { UserAccountsTable } from '../components/UserAccountsTable'

export default function AllUsers() {
  const { data, isLoading } = useAllUsersQuery()

  if (isLoading) {
    return <div>Fetching users...</div>
  }

  return (
    <div className='mt-8 mx-24 space-y-4'>
      <p className='text-2xl'>All Users</p>
      <div className='bg-white shadow-md rounded-md p-2'>
        <UserAccountsTable users={data!} />
      </div>
    </div>
  )
}
