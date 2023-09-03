import { zodResolver } from '@hookform/resolvers/zod'
import * as z from 'zod'
import { Button } from '@/shadcnui/ui/button'
import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from '@/shadcnui/ui/form'
import { Input } from '@/shadcnui/ui/input'
import { Textarea } from '@/shadcnui/ui/textarea'
import { ReloadIcon } from '@radix-ui/react-icons'
import { useForm } from 'react-hook-form'
import { useCreateDepartmentMutation } from '../api/departmentApiSlice'
import { useNavigate } from 'react-router-dom'
import { useDispatch } from 'react-redux'
import { showErrorBanner, showSuccessBanner } from '@/store/bannerSlice'

const schema = z.object({
  name: z.string().min(6).max(128),
  code: z
    .string()
    .min(3)
    .max(8)
    .regex(new RegExp('^[A-Za-z]*$'), 'Code must contain only alphabets'),
  description: z.string().nonempty(),
})

export default function CreateDepartment() {
  const [createDepartment, { isLoading }] = useCreateDepartmentMutation()
  const navigate = useNavigate()
  const dispatch = useDispatch()

  const form = useForm<z.infer<typeof schema>>({
    resolver: zodResolver(schema),
    defaultValues: {
      name: '',
      code: '',
      description: '',
    },
  })

  async function onSubmit(values: z.infer<typeof schema>) {
    try {
      await createDepartment(values).unwrap()
      dispatch(showSuccessBanner('Department created successfully'))
      navigate('/departments/')
    } catch (err) {
      dispatch(showErrorBanner('An error occured while trying to create department'))
      console.log(err)
    }
  }
  return (
    <div className='flex flex-col space-y-4 bg-white border-2 mx-auto mt-16 p-4 rounded-md w-1/2'>
      <p className='text-2xl'>Create Department</p>
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
                  <Input placeholder='Choose a code to represent the department' {...field} />
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
            Create
          </Button>
        </form>
      </Form>
    </div>
  )
}
