import RequireAuth from "@/features/auth/components/RequireAuth"
import Root from "@/layout/Root"
import Dashboard from "@/pages/Dashboard"
import Home from "@/pages/Home"
import NotFound from "@/pages/NotFound"
import Signin from "@/pages/Signin"
import Signup from "@/pages/Signup"
import { Routes, Route } from "react-router-dom"


export default function AppRoutes() {
    return <Routes>
        <Route path="/" element={<Root />}>
            <Route index element={<Home />}></Route>
            <Route path="/signin" element={<Signin />}></Route>
            <Route path="/signup" element={<Signup />}></Route>
            <Route element={<RequireAuth />}>
                <Route path="dashboard" element={<Dashboard />}></Route>
            </Route>
            <Route path="*" element={<NotFound />}></Route>
        </Route>
    </Routes >
}