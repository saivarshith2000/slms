import { RootState } from '@/store'
import { createSlice } from '@reduxjs/toolkit'

type bannerSliceState = {
  msg: string
  isOpen: boolean
  isOverridable: boolean
  type?: 'SUCCESS' | 'ERROR'
}

let initialState: bannerSliceState = { msg: '', isOpen: false, isOverridable: true }

function canOverride(isOpen: boolean, isOverridable: boolean, newMsg: string) {
  if (isOpen && !isOverridable) {
    console.log(`Discarding banner for ${newMsg}. A non-overridable banner is currently open.`)
    return false
  }
  return true
}

export const bannerSlice = createSlice({
  name: 'banner',
  initialState,
  reducers: {
    showSuccessBanner: (state, action) => {
      if (!canOverride(state.isOpen, state.isOverridable, action.payload.msg)) {
        return
      }
      state.msg = action.payload
      state.type = 'SUCCESS'
      state.isOpen = true
      state.isOverridable = true
    },

    showNonOverridableErrorBanner: (state, action) => {
      state.msg = action.payload
      state.type = 'ERROR'
      state.isOpen = true
      state.isOverridable = false
    },

    showErrorBanner: (state, action) => {
      if (!canOverride(state.isOpen, state.isOverridable, action.payload.msg)) {
        return
      }

      state.msg = action.payload
      state.type = 'ERROR'
      state.isOpen = true
      state.isOverridable = true
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

export const { showSuccessBanner, showNonOverridableErrorBanner, showErrorBanner, closeBanner } =
  bannerSlice.actions
export const selectBanner = (state: RootState) => state.banner
