import { zodResolver } from '@hookform/resolvers/zod'
import * as z from 'zod'
import { Button } from '@/shadcnui/ui/button'
import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from '@/shadcnui/ui/form'
import { Input } from '@/shadcnui/ui/input'
import { Textarea } from '@/shadcnui/ui/textarea'
import { ReloadIcon } from '@radix-ui/react-icons'
import { useForm } from 'react-hook-form'
import { useUpdateDepartmentMutation } from '../api/departmentApiSllice'
import { Navigate, useNavigate, useSearchParams } from 'react-router-dom'
import { useDispatch } from 'react-redux'
import { showErrorBanner, showSuccessBanner } from '@/store/bannerSlice'

const schema = z.object({
  name: z.string().min(6).max(128),
  code: z.string(),
  description: z.string().nonempty(),
})

export default function UpdateDepartment() {
  const [UpdateDepartment, { isLoading }] = useUpdateDepartmentMutation()
  const [searchParams] = useSearchParams()
  const navigate = useNavigate()
  const dispatch = useDispatch()

  const form = useForm<z.infer<typeof schema>>({
    resolver: zodResolver(schema),
    defaultValues: {
      name: searchParams.get('name')!,
      code: searchParams.get('code')!,
      description: searchParams.get('description')!,
    },
  })

  if (!searchParams.has('name') || !searchParams.has('code') || !searchParams.has('description')) {
    return <Navigate to='/departments' />
  }

  async function onSubmit(values: z.infer<typeof schema>) {
    console.log(values)
    try {
      await UpdateDepartment({ ...values }).unwrap()
      dispatch(showSuccessBanner('Department updated successfully'))
      navigate('/departments')
    } catch (err) {
      dispatch(showErrorBanner('An error occured while trying to update department'))
      console.log(err)
    }
  }
  return (
    <div className='flex flex-col space-y-4 bg-white border-2 mx-auto mt-16 p-4 rounded-md w-1/2'>
      <p className='text-2xl'>Update Department</p>
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className='space-y-4'>
          <FormField
            control={form.control}
            name='name'
            render={({ field }) => (
              <FormItem>
                <FormLabel>Name</FormLabel>
                <FormControl>
                  <Input placeholder='Name of the department' {...field} />
                </FormControl>
                <FormMessage className='font-light' />
              </FormItem>
            )}
          />

          <FormField
            control={form.control}
            name='code'
            render={({ field }) => (
              <FormItem>
                <FormLabel>Code</FormLabel>
                <FormControl>
                  <Input disabled {...field} />
                </FormControl>
                <FormMessage className='font-light' />
              </FormItem>
            )}
          />

          <FormField
            control={form.control}
            name='description'
            render={({ field }) => (
              <FormItem>
                <FormLabel>Description</FormLabel>
                <FormControl>
                  <Textarea
                    rows={4}
                    placeholder='A brief description of the department'
                    {...field}
                  />
                </FormControl>
                <FormMessage className='font-light' />
              </FormItem>
            )}
          />

          <Button
            type='submit'
            disabled={isLoading}
            className='bg-blue-500 hover:bg-blue-700 w-full'
          >
            {isLoading && <ReloadIcon className='mr-2 h-4 w-4 animate-spin' />}
            Update
          </Button>
        </form>
      </Form>
    </div>
  )
}
