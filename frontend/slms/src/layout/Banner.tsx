import { closeBanner, selectBanner } from '@/store/bannerSlice'
import { useDispatch, useSelector } from 'react-redux'
import { Cross1Icon } from '@radix-ui/react-icons'
import { Button } from '@/shadcnui/ui/button'

export default function Banner() {
  const banner = useSelector(selectBanner)
  const dispatch = useDispatch()

  if (banner.isOpen === false) {
    return null
  }

  const bg = banner.type === 'ERROR' ? 'bg-red-600' : 'bg-green-600'
  return (
    <div
      className={`flex justify-between items-center px-2 py-1 text-sm text-center text-white ${bg}`}
    >
      <p className='flex-1'>{banner.msg}</p>
      <Button onClick={() => dispatch(closeBanner())} size='sm' variant='ghost'>
        <Cross1Icon />
      </Button>
    </div>
  )
}
