import { RootState } from '@/store'
import { createSlice } from '@reduxjs/toolkit'

type bannerSliceState = {
  msg: string
  isOpen: boolean
  type?: 'SUCCESS' | 'ERROR'
}

let initialState: bannerSliceState = { msg: '', isOpen: false }

export const bannerSlice = createSlice({
  name: 'banner',
  initialState,
  reducers: {
    showSuccessBanner: (state, action) => {
      const { msg } = action.payload
      state.msg = msg
      state.type = 'SUCCESS'
      state.isOpen = true
    },
    showErrorBanner: (state, action) => {
      const { msg } = action.payload
      state.msg = msg
      state.type = 'ERROR'
      state.isOpen = true
    },
    closeBanner: (state) => {
      state.isOpen = false
      state.msg = ''
      state.type = undefined
    },
  },
})

export default bannerSlice.reducer

export const { showSuccessBanner, showErrorBanner, closeBanner } = bannerSlice.actions
export const selectBanner = (state: RootState) => state.banner
