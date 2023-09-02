import { RootState } from '@/store'
import { createSlice } from '@reduxjs/toolkit'
import { User } from '../types'

type authSliceState = {
  user: null | User
  token: null | string
}

let initialState: authSliceState
if (localStorage.getItem('user') === null) {
  initialState = { user: null, token: null }
} else {
  initialState = JSON.parse(localStorage.getItem('user')!)
}

export const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    setCredentials: (state, action) => {
      const { user, token } = action.payload
      state.user = user
      state.token = token
    },
    logOut: (state) => {
      state.user = null
      state.token = null
    },
  },
})

export default authSlice.reducer

export const { setCredentials, logOut } = authSlice.actions
export const selectCurrentUser = (state: RootState) => state.auth.user
export const selectCurrentToken = (state: RootState) => state.auth.token
