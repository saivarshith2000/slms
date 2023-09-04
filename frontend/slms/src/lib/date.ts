import { format } from 'date-fns'

export type DateTimeType = {
  date: string
  time: string
}

export function formatDateTime(datetime: Date): DateTimeType {
  return {
    date: format(datetime, 'dd, MMMM, yyyy'),
    time: format(datetime, 'hh:mm:ss a'),
  }
}
