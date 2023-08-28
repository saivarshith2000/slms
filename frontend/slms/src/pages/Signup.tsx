import { Link } from 'react-router-dom'
import SignUpForm from '@/features/auth/components/SignUpForm'

export default function SignUp() {
  return (
    <div className='flex flex-col w-1/4 m-auto mt-12 gap-4'>
      <div className='flex flex-col bg-white border border-solid border-gray-200 rounded-md p-8 gap-4'>
        <p className='text-3xl'>Sign Up</p>
        <SignUpForm />
      </div>
      <Link to='/signin' className='text-green-600 text-center underline underline-offset-4'>
        Already have an account ?
      </Link>
    </div>
  )
}
