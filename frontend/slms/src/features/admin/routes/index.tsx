import { Route } from 'react-router-dom'
import AllUsers from './AllUsers'
import AdminRoute from '@/routes/AdminRoute'

const AdminRoutes = (
  <Route path='admin' element={<AdminRoute />}>
    <Route path='accounts' index element={<AllUsers />} />
    <Route path='accounts/all' index element={<AllUsers />} />
  </Route>
)

export default AdminRoutes
