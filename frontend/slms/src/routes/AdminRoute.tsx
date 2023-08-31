import { Outlet, Navigate } from 'react-router-dom'
import { useSelector } from 'react-redux/es/hooks/useSelector'
import { selectCurrentUser } from '@/features/auth/store/authSlice'

export default function AdminRoute() {
  const user = useSelector(selectCurrentUser)
  if (user === null) return <Navigate to='/auth/signin' replace />
  if (user.role != 'ADMIN') return <Navigate to='/' />
  return <Outlet />
}
