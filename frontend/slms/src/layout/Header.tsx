import { logOut, selectCurrentUser } from '@/features/auth/store/authSlice'
import { User } from '@/features/auth/types'
import { Button } from '@/shadcnui/ui/button'
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from '@/shadcnui/ui/dropdown-menu'
import { useDispatch, useSelector } from 'react-redux'
import { Link, useNavigate } from 'react-router-dom'

export function Profile({ user }: { user: User }) {
  const dispatch = useDispatch()
  const navigate = useNavigate()

  function handleLogout() {
    dispatch(logOut({}))
    navigate('/auth/signin', { replace: true })
  }

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant='ghost'>Hi, {user.first_name}</Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent>
        <DropdownMenuItem>Profile</DropdownMenuItem>
        <DropdownMenuItem onClick={handleLogout}>Logout</DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  )
}

export default function Header() {
  const user = useSelector(selectCurrentUser)

  return (
    <div className='flex flex-row justify-between align-middle px-24 py-2 bg-white border-b-gray-200 border-b border-solid'>
      <p className='text-xl my-auto'>
        <Link to='/'>SLMS</Link>
      </p>

      {user ? (
        <div className='flex flex-row space-evenly gap-2'>
          <Link to='/departments'>
            <Button variant='ghost'>Departments</Button>
          </Link>
          <Profile user={user!} />
        </div>
      ) : (
        <div>
          <Link to='/departments'>
            <Button variant='ghost'>Departments</Button>
          </Link>
          <Link to='/auth/signin'>
            <Button variant='ghost'>Sign In</Button>
          </Link>
        </div>
      )}
    </div>
  )
}
