import { selectBanner } from '@/store/bannerSlice'
import { useSelector } from 'react-redux'

export default function Banner() {
  const banner = useSelector(selectBanner)

  if (!banner.isOpen || banner.type === undefined) {
    return null
  }
  if (banner.type == 'ERROR') {
    return <div className='px-2 py-1 text-sm text-center bg-red-600 text-white'>{banner.msg}</div>
  }

  return <div className='px-2 py-1 text-sm text-center bg-green-600 text-white'>{banner.msg}</div>
}
