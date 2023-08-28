import { useNavigate } from 'react-router-dom'
import SignUpForm from '../components/SignUpForm'
import Layout from '../components/Layout'

export default function SignUp() {
  const navigate = useNavigate()

  return (
    <Layout alternateLink='/auth/signin' alternateText='Have an account ?'>
      <SignUpForm onSuccess={() => navigate('/signin')} />
    </Layout>
  )
}
