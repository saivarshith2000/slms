export interface ApiError {
  status: number
  data: { detail: string }
}

export function isApiError(error: unknown): error is ApiError {
  return (
    typeof error === 'object' &&
    error != null &&
    'status' in error &&
    typeof (error as any).status === 'number'
  )
}
