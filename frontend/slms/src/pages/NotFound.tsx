import { Link } from 'react-router-dom'

export default function NotFound() {
  return (
    <div className='flex flex-col m-auto text-center gap-4'>
      <p className='text-8xl font-extralight mt-24'>Page Not Found</p>
      <p className='text-lg text-gray-700'>
        <Link to='/' className='underline underline-offset-4'>
          Go back home
        </Link>
      </p>
    </div>
  )
}
