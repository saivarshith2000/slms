import { zodResolver } from '@hookform/resolvers/zod'
import * as z from 'zod'
import { Button } from '@/shadcnui/ui/button'
import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from '@/shadcnui/ui/form'
import { Input } from '@/shadcnui/ui/input'
import { ReloadIcon } from '@radix-ui/react-icons'
import { useForm } from 'react-hook-form'
import { useDispatch } from 'react-redux'
import { setCredentials } from '../store/authSlice'
import { useSigninMutation } from '../store/authApiSlice'
import { useNavigate } from 'react-router-dom'

const schema = z.object({
  email: z.string().email(),
  password: z.string().min(6).max(64),
})

export default function SignInForm() {
  const [signin, { isLoading }] = useSigninMutation()
  const dispatch = useDispatch()
  const navigate = useNavigate()

  const form = useForm<z.infer<typeof schema>>({
    resolver: zodResolver(schema),
  })

  async function onSubmit(values: z.infer<typeof schema>) {
    console.log(values)
    try {
      const { access_token, user } = await signin({ ...values }).unwrap()
      dispatch(setCredentials({ token: access_token, user }))
      navigate('/dashboard')
    } catch (err) {
      console.log(err)
    }
  }
  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className='space-y-4'>
        <FormField
          control={form.control}
          name='email'
          render={({ field }) => (
            <FormItem>
              <FormLabel>Email</FormLabel>
              <FormControl>
                <Input placeholder='Your email address' {...field} type='email' />
              </FormControl>
              <FormMessage className='font-light' />
            </FormItem>
          )}
        />

        <FormField
          control={form.control}
          name='password'
          render={({ field }) => (
            <FormItem>
              <FormLabel>Password</FormLabel>
              <FormControl>
                <Input placeholder='Your Password' {...field} type='password' />
              </FormControl>
              <FormMessage className='font-light' />
            </FormItem>
          )}
        />

        <Button type='submit' disabled={isLoading} className='bg-blue-500 hover:bg-blue-700 w-full'>
          {isLoading && <ReloadIcon className='mr-2 h-4 w-4 animate-spin' />}
          Sign In
        </Button>
      </form>
    </Form>
  )
}
