import { BaseQueryFn, createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'
import { logOut } from '@/features/auth/store/authSlice'
import { RootState } from '.'
import { showNonOverridableErrorBanner } from './bannerSlice'
import { isApiError } from '@/types'

const baseQuery = fetchBaseQuery({
  // baseUrl: `${import.meta.env.BACKEND_URL}/api/v1`,
  baseUrl: 'http://localhost:8000/api/v1',
  credentials: 'include',
  prepareHeaders: (headers, { getState }) => {
    const state = getState() as RootState
    const token = state.auth.token
    if (token) {
      headers.set('authorization', `Bearer ${token}`)
    }
    return headers
  },
})

const baseQueryWithReauth: BaseQueryFn = async (args, api, extraOptions) => {
  // TODO
  // Implement token refresh on the backend and update this function accordingly

  const result = await baseQuery(args, api, extraOptions)

  if (result?.error?.status === 401 && (api.getState() as RootState).auth.user != null) {
    console.log('Token expired. Logging out')
    api.dispatch(showNonOverridableErrorBanner('Session expired. Please signin again'))
    api.dispatch(logOut())
  } else if (isApiError(result.error)) {
    // This catches all other expected errors
    api.dispatch(showNonOverridableErrorBanner(result.error.data?.detail))
  }
  return result
}

export const apiSlice = createApi({
  baseQuery: baseQueryWithReauth,
  endpoints: (_) => ({}),
})
