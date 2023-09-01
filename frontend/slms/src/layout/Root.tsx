import { Outlet } from 'react-router-dom'
import Header from './Header'
import Banner from './Banner'

export default function Root() {
  return (
    <>
      <Header />
      <Banner />
      <Outlet />
    </>
  )
}
