import { configureStore } from "@reduxjs/toolkit";
import { apiSlice } from "./apiSlice";
import authReducer from "@/features/auth/store/authSlice";
import { setupListeners } from "@reduxjs/toolkit/dist/query";
import authMiddleware from "@/features/auth/store/authMiddleware";


export const store = configureStore({
    reducer: {
        [apiSlice.reducerPath]: apiSlice.reducer,
        auth: authReducer,
    },
    middleware: (getDefaultMiddleware) =>
        getDefaultMiddleware()
            .prepend(authMiddleware.middleware)
            .concat(apiSlice.middleware),
    devTools: true,
})

// For refetchOnFocus behaviour
setupListeners(store.dispatch)

// Infer the `RootState` and `AppDispatch` types from the store itself
export type RootState = ReturnType<typeof store.getState>
// Inferred type: {posts: PostsState, comments: CommentsState, users: UsersState}
export type AppDispatch = typeof store.dispatch
