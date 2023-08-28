import SignIn from './SignIn'
import SignUp from './SignUp'

const authRoutes = {
  path: 'auth',
  children: [
    {
      path: 'signin',
      element: <SignIn />,
    },
    {
      path: 'signup',
      element: <SignUp />,
    },
  ],
}

export default authRoutes
