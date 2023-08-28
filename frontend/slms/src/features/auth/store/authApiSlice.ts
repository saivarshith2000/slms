import { apiSlice } from '@/store/apiSlice'
import { SignInInput, SignInResponse } from '../types'

export const authApiSlice = apiSlice.injectEndpoints({
  endpoints: (builder) => ({
    signin: builder.mutation<SignInResponse, SignInInput>({
      query: (credentials) => {
        const formData = new FormData()
        formData.append('username', credentials.email)
        formData.append('password', credentials.password)
        return {
          url: '/auth/signin',
          method: 'POST',
          body: formData,
        }
      },
    }),
  }),
})

export const { useSigninMutation } = authApiSlice
