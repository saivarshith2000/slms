import { Route } from 'react-router-dom'
import ListDepartments from './ListDepartments'
import CreateDepartment from './CreateDepartment'
import AdminRoute from '@/routes/AdminRoute'
import UpdateDepartment from './UpdateDepartment'

const DepartmentRoutes = (
  <Route path='departments'>
    <Route path='' index element={<ListDepartments />} />
    <Route path='' element={<AdminRoute />}>
      <Route path='create' element={<CreateDepartment />} />
      <Route path='update' element={<UpdateDepartment />} />
    </Route>
  </Route>
)

export default DepartmentRoutes
