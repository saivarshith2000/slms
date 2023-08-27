import { zodResolver } from "@hookform/resolvers/zod"
import * as z from "zod"
import { Button } from "@/shadcnui/ui/button"
import {
    Form,
    FormControl,
    FormField,
    FormItem,
    FormLabel,
    FormMessage,
} from "@/shadcnui/ui/form"
import { Input } from "@/shadcnui/ui/input"
import { useForm } from "react-hook-form"
import { SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/shadcnui/ui/select"
import { Select } from "@radix-ui/react-select"

const schema = z.object({
    first_name: z.string().min(6).max(32),
    last_name: z.string().min(6).max(32),
    email: z.string().email(),
    role: z.string().min(1),
    password: z.string().min(6).max(64),
    confirm_password: z.string().min(6).max(64)
})

export default function SignUpForm() {
    const form = useForm<z.infer<typeof schema>>({
        resolver: zodResolver(schema),
    })

    function onSubmit(values: z.infer<typeof schema>) {
        // Do something with the form values.
        console.log(values)
    }
    return (
        <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
                <FormField
                    control={form.control}
                    name="first_name"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>First Name</FormLabel>
                            <FormControl>
                                <Input placeholder="First Name" {...field} type="text" />
                            </FormControl>
                            <FormMessage className="font-light" />
                        </FormItem>
                    )}
                />
                <FormField
                    control={form.control}
                    name="last_name"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Last Name</FormLabel>
                            <FormControl>
                                <Input placeholder="Last Name" {...field} type="text" />
                            </FormControl>
                            <FormMessage className="font-light" />
                        </FormItem>
                    )}
                />

                <FormField
                    control={form.control}
                    name="email"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Email</FormLabel>
                            <FormControl>
                                <Input placeholder="Your Email Address" {...field} type="email" />
                            </FormControl>
                            <FormMessage className="font-light" />
                        </FormItem>
                    )}
                />

                <FormField
                    control={form.control}
                    name="password"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Password</FormLabel>
                            <FormControl>
                                <Input placeholder="Your Password" {...field} type="password" />
                            </FormControl>
                            <FormMessage className="font-light" />
                        </FormItem>
                    )}
                />


                <FormField
                    control={form.control}
                    name="role"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Role</FormLabel>
                            <Select onValueChange={field.onChange} defaultValue={field.value}>
                                <FormControl>
                                    <SelectTrigger>
                                        <SelectValue placeholder="Select Your Role" />
                                    </SelectTrigger>
                                </FormControl>
                                <SelectContent>
                                    <SelectItem value="STUDENT">Student</SelectItem>
                                    <SelectItem value="TEACHER">Teacher</SelectItem>
                                </SelectContent>
                            </Select>
                        </FormItem>
                    )}
                />

                <FormField
                    control={form.control}
                    name="confirm_password"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Confirm Password</FormLabel>
                            <FormControl>
                                <Input placeholder="Confirm Your Password" {...field} type="password" />
                            </FormControl>
                            <FormMessage className="font-light" />
                        </FormItem>
                    )}
                />


                <Button type="submit" className="bg-green-500 hover:bg-green-700 w-full">Sign In</Button>
            </form>
        </Form>
    )

}