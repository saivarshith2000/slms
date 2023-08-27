import { useLocation, Navigate, Outlet } from "react-router-dom";
import { UseSelector, useSelector } from "react-redux/es/hooks/useSelector";
import { selectCurrentToken } from "../store/authSlice";


export default function RequireAuth() {
    const token = useSelector(selectCurrentToken)
    const location = useLocation()

    return (
        token
            ? <Outlet />
            : <Navigate to="/signin" state={{ from: location }} replace />
    )

}

