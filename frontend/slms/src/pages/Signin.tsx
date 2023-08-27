import { Link } from "react-router-dom"
import SignInForm from "@/features/auth/components/SignInForm"

export default function SignIn() {
    return <div className="flex flex-col gap-4 mx-4 mt-16">
        <div className="flex flex-col bg-white border border-solid border-gray-200 rounded-md p-8 gap-4 lg:w-1/3 md:w-1/2 w-full m-auto">
            <p className="text-3xl">Sign In</p>
            <SignInForm />
        </div>
        <Link to="/signup" className="text-blue-600 text-center underline underline-offset-4">Don't have an account ?</Link>
    </div>

}
