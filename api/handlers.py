from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.models import UserCreate, ShowUser, UpdateUserRequest, DeleteUserResponse
from db.dals import UserDAL
from db.session import get_db

user_router = APIRouter(prefix="/user", tags=["user"])


async def _create_new_user(body: UserCreate, db: AsyncSession) -> ShowUser:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            user = await user_dal.create_user(
                name=body.name,
                surname=body.surname,
                email=body.email
            )

            if not user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {user} not found.")

            return ShowUser.model_validate(user)


async def _delete_user(user_id: UUID, db: AsyncSession) -> Optional[ShowUser]:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            user_id = await user_dal.delete_user(user_id=user_id)

            if not user_id:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {user_id} not found.")

            return user_id


async def _get_user_by_id(user_id: UUID, db: AsyncSession) -> Optional[ShowUser]:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            user = await user_dal.get_user_by_id(user_id=user_id)

            if not user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {user} not found.")

            return ShowUser.model_validate(user)


async def _update_user(user_id: UUID, body: UpdateUserRequest, db: AsyncSession) -> Optional[ShowUser]:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            body = body.model_dump(exclude_none=True)
            user = await user_dal.update_user(
                user_id=user_id,
                **body
            )

            if not user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {user} not found.")

            return ShowUser.model_validate(user)


@user_router.post('/', response_model=ShowUser)
async def create_user(body: UserCreate, db: AsyncSession = Depends(get_db)) -> ShowUser:
    return await _create_new_user(body, db)


@user_router.delete('/', response_model=DeleteUserResponse)
async def delete_user(user_id: UUID, db: AsyncSession = Depends(get_db)) -> DeleteUserResponse:
    deleted_user_id = await _delete_user(user_id, db)
    return DeleteUserResponse(user_id=deleted_user_id)


@user_router.get('/', response_model=ShowUser)
async def get_user_by_id(user_id: UUID, db: AsyncSession = Depends(get_db)) -> ShowUser:
    user = await _get_user_by_id(user_id, db)
    return user


@user_router.put('/', response_model=ShowUser)
async def update_user(user_id: UUID, body: UpdateUserRequest, db: AsyncSession = Depends(get_db)) -> ShowUser:
    if not body.model_dump(exclude_none=True):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="At least one parameter for user update info should be provided")
    user = await _update_user(user_id, body, db)
    return user
