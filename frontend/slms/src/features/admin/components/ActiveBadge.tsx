type ActiveBadgeType = {
  active: boolean
}

export default function ActiveBadge({ active }: ActiveBadgeType) {
  let text_color = 'text-orange-400'
  let border_color = 'border-orange-400'
  let text = 'PENDING'

  if (active) {
    text_color = 'text-green-400'
    border_color = 'border-green-400'
    text = 'YES'
  }

  return (
    <span
      className={`text-[11px] font-bold p-0.5 px-1 rounded-md border-2 ${border_color} ${text_color}`}
    >
      {text}
    </span>
  )
}
