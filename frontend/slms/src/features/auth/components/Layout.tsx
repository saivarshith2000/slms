import { Link } from 'react-router-dom'

type LayoutProps = {
  children: React.ReactNode
  title: string
  alternateLink: string
  alternateText: string
}

export default function Layout(props: LayoutProps) {
  return (
    <div className='flex flex-col gap-4 mx-4 mt-16'>
      <div className='flex flex-col bg-white border border-solid border-gray-200 rounded-md p-8 gap-4 lg:w-1/3 md:w-1/2 w-full m-auto'>
        <p className='text-3xl'>{props.title}</p>
        {props.children}
      </div>
      <Link
        to={props.alternateLink}
        className='text-blue-600 text-center underline underline-offset-4'
      >
        {props.alternateText}
      </Link>
    </div>
  )
}
