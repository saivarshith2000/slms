import { apiSlice } from '@/store/apiSlice'
import { SignInInput, SignInResponse, SignUpInput } from '../types'

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

    signup: builder.mutation<string, SignUpInput>({
      query: (credentials) => {
        return {
          url: '/auth/signup',
          method: 'POST',
          body: { ...credentials },
        }
      },
    }),
  }),
})

export const { useSigninMutation, useSignupMutation } = authApiSlice
