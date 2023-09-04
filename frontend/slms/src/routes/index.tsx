import RequireAuth from '@/features/auth/components/RequireAuth'
import Root from '@/layout/Root'
import Dashboard from '@/pages/Dashboard'
import Landing from '@/pages/Landing'
import NotFound from '@/pages/NotFound'
import { Route, Routes } from 'react-router-dom'
import AuthRoutes from '@/features/auth/routes'
import DepartmentRoutes from '@/features/department/routes'
import AdminRoutes from '@/features/admin/routes'

export default function AppRoutes() {
  return (
    <Routes>
      <Route path='/' element={<Root />}>
        <Route path='' index element={<Landing />} />
        {AuthRoutes}
        {DepartmentRoutes}
        {AdminRoutes}
        <Route path='/admin/dashboard' element={<RequireAuth />}>
          <Route path='' element={<Dashboard />} />
        </Route>
        <Route path='*' element={<NotFound />}></Route>
      </Route>
    </Routes>
  )
}
