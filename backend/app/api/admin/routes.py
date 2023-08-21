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
async def all_accounts_route(db_session: DBSession):
    return await get_all_accounts(db_session)


@router.get("/accounts/pending", response_model=List[BaseUserSchema])
async def pending_accounts_route(db_session: DBSession):
    return await get_inactive_accounts(db_session)


@router.post("/accounts/activate")
async def activate_account_route(request: AccountActivationRequestSchema, db_session: DBSession):
    logger.info(f"Activating user account - {request.email}")
    await activate_account(request.email, request.department, db_session)
    return {"message": "Account activated successfully"}


@router.post("/accounts/deactivate")
async def deactivate_account_route(email: str, db_session: DBSession):
    logger.info(f"Dectivating user account - {email}")
    await deactivate_account(email, db_session)
    return {"message": "Account de-activated successfully"}


@router.post("/departments/create", response_model=DepartmentSchema)
async def create_department_route(request: DepartmentSchema, db_session: DBSession):
    logger.info(f"Creating department - {request.name} - {request.abbreviation}")
    return await create_department(request, db_session)


@router.put("/departments/update/{abbr}", response_model=DepartmentSchema)
async def update_department_route(abbr: str, request: UpdateDepartmentSchema, db_session: DBSession):
    logger.info(f"Updating department - {abbr}")
    return await update_department(abbr, request, db_session)


@router.delete("/departments/delete")
async def delete_department_route():
    # TODO: Involves updating each user of the department.
    # Will implement later if required
    raise NotImplementedError
