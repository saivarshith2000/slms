import { useSelector } from 'react-redux'
import { selectCurrentUser } from '@/features/auth/store/authSlice'

import { Link } from 'react-router-dom'

export default function Dashboard() {
  const user = useSelector(selectCurrentUser)

  return (
    <div>
      <p>
        Welcome {user?.first_name}, {user?.last_name}
      </p>
      <p>It seems you are an admin!</p>
    </div>
  )
}
