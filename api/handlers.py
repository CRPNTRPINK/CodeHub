from typing import Optional
from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from api.models import DeleteUserResponse
from api.models import ShowUser
from api.models import UpdateUserRequest
from api.models import UserCreate
from db.dals import UserDAL
from db.models import User
from db.session import get_db

user_router = APIRouter(prefix="/user", tags=["user"])


async def _create_new_user(body: UserCreate, db: AsyncSession) -> User:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            user = await user_dal.create_user(
                name=body.name, surname=body.surname, email=body.email
            )

            return user


async def _delete_user(user_id: UUID, db: AsyncSession) -> Optional[UUID]:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            user_id = await user_dal.delete_user(user_id=user_id)

            return user_id


async def _get_user_by_id(user_id: UUID, db: AsyncSession) -> Optional[User]:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            user = await user_dal.get_user_by_id(user_id=user_id)

            return user


async def _update_user(
    user_id: UUID, body: UpdateUserRequest, db: AsyncSession
) -> Optional[User]:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            body = body.model_dump(exclude_none=True)
            user = await user_dal.update_user(user_id=user_id, **body)

            return user


@user_router.post("/", response_model=ShowUser)
async def create_user(body: UserCreate, db: AsyncSession = Depends(get_db)) -> ShowUser:
    try:
        user = await _create_new_user(body, db)
    except IntegrityError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=e.args[0])

    return ShowUser.model_validate(user)


@user_router.delete("/", response_model=DeleteUserResponse)
async def delete_user(
    user_id: UUID, db: AsyncSession = Depends(get_db)
) -> DeleteUserResponse:
    deleted_user_id = await _delete_user(user_id, db)

    if not deleted_user_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id: {user_id} not found.",
        )

    return DeleteUserResponse(user_id=deleted_user_id)


@user_router.get("/", response_model=ShowUser)
async def get_user_by_id(user_id: UUID, db: AsyncSession = Depends(get_db)) -> ShowUser:
    user = await _get_user_by_id(user_id, db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id: {user} not found.",
        )

    return ShowUser.model_validate(user)


@user_router.put("/", response_model=ShowUser)
async def update_user(
    user_id: UUID, body: UpdateUserRequest, db: AsyncSession = Depends(get_db)
) -> ShowUser:
    if not body.model_dump(exclude_none=True):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="At least one parameter for user update info should be provided",
        )

    try:
        user = await _update_user(user_id, body, db)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"user with id: {user} not found.",
            )
    except IntegrityError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=e.args[0])

    return ShowUser.model_validate(user)
