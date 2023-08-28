import { createListenerMiddleware } from '@reduxjs/toolkit'
import { logOut, setCredentials } from './authSlice'

const authMiddleware = createListenerMiddleware()
authMiddleware.startListening({
  actionCreator: setCredentials,
  effect: (action, _) => {
    console.log('Saving user to localStorage')
    localStorage.setItem('user', JSON.stringify(action.payload))
  },
})

authMiddleware.startListening({
  actionCreator: logOut,
  effect: (_1, _2) => {
    console.log('Clearing localStorage')
    localStorage.removeItem('user')
  },
})

export default authMiddleware
