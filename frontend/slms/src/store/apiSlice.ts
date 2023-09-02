import { BaseQueryFn, createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'
import { logOut } from '@/features/auth/store/authSlice'
import { RootState } from '.'
import { showErrorBanner } from './bannerSlice'

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

  if (result?.error?.status === 401) {
    console.log('Token expired. Logging out')
    api.dispatch(
      showErrorBanner({ msg: 'Session expired. Please signin again', isOverridable: false }),
    )
    api.dispatch(logOut())
  }
  return result
}

export const apiSlice = createApi({
  baseQuery: baseQueryWithReauth,
  endpoints: (_) => ({}),
})
