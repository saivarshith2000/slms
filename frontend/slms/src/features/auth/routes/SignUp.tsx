import { useNavigate } from 'react-router-dom'
import SignUpForm from '../components/SignUpForm'
import Layout from '../components/Layout'

export default function SignUp() {
  const navigate = useNavigate()

  return (
    <Layout alternateLink='/auth/signin' alternateText='Have an account ?' title='Sign Up'>
      <SignUpForm onSuccess={() => navigate('/auth/signin')} />
    </Layout>
  )
}
