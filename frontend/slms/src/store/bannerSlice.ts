import { RootState } from '@/store'
import { createSlice } from '@reduxjs/toolkit'

type bannerSliceState = {
  msg: string
  isOpen: boolean
  isOverridable?: boolean
  type?: 'SUCCESS' | 'ERROR'
}

let initialState: bannerSliceState = { msg: '', isOpen: false, isOverridable: true }

export const bannerSlice = createSlice({
  name: 'banner',
  initialState,
  reducers: {
    showSuccessBanner: (state, action) => {
      if (state.isOpen && !state.isOverridable) {
        console.log(
          `Discarding success banner for ${state.msg}. A non-overridable banner is currently open.`,
        )
        return
      }
      const { msg, isOverridable = true } = action.payload
      state.msg = msg
      state.type = 'SUCCESS'
      state.isOpen = true
      state.isOverridable = isOverridable
    },

    showErrorBanner: (state, action) => {
      if (state.isOpen && !state.isOverridable) {
        console.log(
          `Discarding error banner for ${state.msg}. A non-overridable banner is currently open.`,
        )
        return
      }

      const { msg, isOverridable = true } = action.payload
      state.msg = msg
      state.type = 'ERROR'
      state.isOpen = true
      state.isOverridable = isOverridable
    },
    closeBanner: (state) => {
      state.isOpen = false
      state.msg = ''
      state.type = undefined
      state.isOverridable = true
    },
  },
})

export default bannerSlice.reducer

export const { showSuccessBanner, showErrorBanner, closeBanner } = bannerSlice.actions
export const selectBanner = (state: RootState) => state.banner
