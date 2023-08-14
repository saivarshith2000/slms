from typing import List
from fastapi import APIRouter, Depends

from app.db import AsyncSession
from app.api.departments.schema import DepartmentSchema

from .schema import AccountActivationRequestSchema, UpdateDepartmentSchema
from .service import (
    get_all_accounts,
    get_inactive_accounts,
    activate_account,
    deactivate_account,
    create_department,
    update_department,
)
from .dependencies import is_admin

from ..auth.schema import BaseUserSchema

router = APIRouter(prefix="/admin", dependencies=[Depends(is_admin)])


@router.get("/accounts/all", response_model=List[BaseUserSchema])
async def pending_accounts_route(async_session: AsyncSession):
    return await get_all_accounts(async_session)


@router.get("/accounts/pending", response_model=List[BaseUserSchema])
async def pending_accounts_route(async_session: AsyncSession):
    return await get_inactive_accounts(async_session)


@router.post("/accounts/activate")
async def activate_account_route(
    request: AccountActivationRequestSchema, async_session: AsyncSession
):
    await activate_account(request.email, request.department, async_session)
    return {"message": "Account activated successfully"}


@router.post("/accounts/deactivate/:email")
async def deactivate_account_route(email: str, async_session: AsyncSession):
    await deactivate_account(email, async_session)
    return {"message": "Account de-activated successfully"}


@router.post("/departments/create", response_model=DepartmentSchema)
async def create_department_route(
    request: DepartmentSchema, async_session: AsyncSession
):
    return await create_department(request, async_session)


@router.post("/departments/update/:abbr", response_model=DepartmentSchema)
async def update_department_route(
    abbr: str, request: UpdateDepartmentSchema, async_session: AsyncSession
):
    return await update_department(abbr, request, async_session)


@router.delete("/departments/delete")
async def delete_department_route():
    # TODO: Involves updating each user of the department.
    # Will implement later if required
    raise NotImplementedError
