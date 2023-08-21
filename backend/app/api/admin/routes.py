from typing import List

from fastapi import APIRouter, Depends

from app.api.departments.schema import DepartmentSchema
from app.core.log import logger
from app.db import DBSession

from ..auth.schema import BaseUserSchema
from .dependencies import is_admin
from .schema import AccountActivationRequestSchema, UpdateDepartmentSchema
from .service import (
    activate_account,
    create_department,
    deactivate_account,
    get_all_accounts,
    get_inactive_accounts,
    update_department,
)

router = APIRouter(prefix="/admin", dependencies=[Depends(is_admin)])


@router.get("/accounts/all", response_model=List[BaseUserSchema])
async def all_accounts_route(session: DBSession):
    return await get_all_accounts(session)


@router.get("/accounts/pending", response_model=List[BaseUserSchema])
async def pending_accounts_route(session: DBSession):
    return await get_inactive_accounts(session)


@router.post("/accounts/activate")
async def activate_account_route(request: AccountActivationRequestSchema, session: DBSession):
    logger.info(f"Activating user account - {request.email}")
    await activate_account(request.email, request.department_code, session)
    return {"message": "Account activated successfully"}


@router.post("/accounts/deactivate")
async def deactivate_account_route(email: str, session: DBSession):
    logger.info(f"Dectivating user account - {email}")
    await deactivate_account(email, session)
    return {"message": "Account de-activated successfully"}


@router.post("/departments/create", response_model=DepartmentSchema)
async def create_department_route(request: DepartmentSchema, session: DBSession):
    logger.info(f"Creating department - {request.name} - {request.code}")
    return await create_department(request, session)


@router.put("/departments/update/{code}", response_model=DepartmentSchema)
async def update_department_route(code: str, request: UpdateDepartmentSchema, session: DBSession):
    logger.info(f"Updating department - {code}")
    return await update_department(code, request, session)


@router.delete("/departments/delete")
async def delete_department_route():
    # TODO: Involves updating each user of the department.
    # Will implement later if required
    raise NotImplementedError
