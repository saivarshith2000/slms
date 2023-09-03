import { useNavigate } from 'react-router-dom'
import SignInForm from '../components/SignInForm'
import Layout from '../components/Layout'

export default function SignIn() {
  const navigate = useNavigate()

  return (
    <Layout alternateLink='/auth/signup' alternateText="Don't have an account?" title='Sign In'>
      <SignInForm onSuccess={(role: string) => navigate(`/${role}/dashboard`)} />
    </Layout>
  )
}
