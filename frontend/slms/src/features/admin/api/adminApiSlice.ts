import { apiSlice } from '@/store/apiSlice'
import { UserAccount } from '../types'

const taggedApiSlice = apiSlice.enhanceEndpoints({
  addTagTypes: ['users'],
})

export const adminApiSlice = taggedApiSlice.injectEndpoints({
  endpoints: (builder) => ({
    allUsers: builder.query<UserAccount[], void>({
      query: () => {
        return {
          url: '/admin/accounts/all',
          method: 'GET',
        }
      },
    }),
    pendingUsers: builder.query<UserAccount[], void>({
      query: () => {
        return {
          url: '/admin/accounts/pending',
          method: 'GET',
        }
      },
    }),
  }),
})

export const { useAllUsersQuery, usePendingUsersQuery } = adminApiSlice
