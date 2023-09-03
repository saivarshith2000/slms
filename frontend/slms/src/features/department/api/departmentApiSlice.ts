import { apiSlice } from '@/store/apiSlice'
import { Department, DepartmentDetail } from '../types'

const taggedApiSlice = apiSlice.enhanceEndpoints({
  addTagTypes: ['departments'],
})

export const departmentApiSlice = taggedApiSlice.injectEndpoints({
  endpoints: (builder) => ({
    allDepartments: builder.query<Department[], void>({
      providesTags: ['departments'],
      query: () => {
        return {
          url: '/departments/all',
          method: 'GET',
        }
      },
    }),
    departmentDetails: builder.query<DepartmentDetail, string>({
      query: (code: string) => {
        return {
          url: `/departments/${code}`,
          method: 'GET',
        }
      },
    }),
    createDepartment: builder.mutation<Department, Department>({
      invalidatesTags: ['departments'],
      query: (data: Department) => {
        return {
          url: '/admin/departments/create',
          method: 'POST',
          body: data,
        }
      },
    }),
    updateDepartment: builder.mutation<Department, Department>({
      invalidatesTags: ['departments'],
      query: (data: Department) => {
        return {
          url: `/admin/departments/${data.code}/update`,
          method: 'PUT',
          body: { name: data.name, description: data.description },
        }
      },
    }),
  }),
})

export const {
  useCreateDepartmentMutation,
  useUpdateDepartmentMutation,
  useAllDepartmentsQuery,
  useDepartmentDetailsQuery,
} = departmentApiSlice
