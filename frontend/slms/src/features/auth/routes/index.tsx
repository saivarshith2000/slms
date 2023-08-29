import { Route } from 'react-router-dom'
import SignIn from './SignIn'
import SignUp from './SignUp'

const AuthRoutes = (
  <Route path='auth'>
    <Route path='signin' element={<SignIn />} />
    <Route path='signup' element={<SignUp />} />
  </Route>
)

export default AuthRoutes
