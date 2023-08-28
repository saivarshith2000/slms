import RequireAuth from '@/features/auth/components/RequireAuth'
import Root from '@/layout/Root'
import Dashboard from '@/pages/Dashboard'
import Landing from '@/pages/Landing'
import NotFound from '@/pages/NotFound'
import authRoutes from '@/features/auth/routes'

const AppRoutes = [
  {
    path: '/',
    element: <Root />,
    children: [
      {
        path: '',
        element: <Landing />,
      },
      authRoutes,
      {
        path: '/admin',
        element: <RequireAuth />,
        children: [
          {
            path: 'dashboard',
            element: <Dashboard />,
          },
        ],
      },
      {
        path: '*',
        element: <NotFound />,
      },
    ],
  },
]

export default AppRoutes
