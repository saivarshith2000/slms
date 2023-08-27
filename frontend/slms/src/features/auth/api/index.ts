import customBaseQuery from '@/store/customBaseQuery';
import { createApi } from '@reduxjs/toolkit/query/react';
import { SignUpInput } from '../types';


export const authApi = createApi({
    reducerPath: 'authApi',
    baseQuery: customBaseQuery,
    endpoints: builder => ({
        signup: builder.mutation<string, SignUpInput>({
            query(data) {
                return {
                    url: 'auth/register',
                    method: 'POST',
                    body: data,
                };
            },
        }),
    })
})