from uuid import UUID
import re
from typing import Optional

from fastapi import HTTPException, status
from pydantic import BaseModel, EmailStr, field_validator

LATTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z\-]+$")


class TunedModel(BaseModel):
    class Config:
        from_attributes = True


class ShowUser(TunedModel):
    user_id: UUID
    name: str
    surname: str
    email: EmailStr
    is_active: bool


class UserCreate(BaseModel):
    name: str
    surname: str
    email: Optional[EmailStr]

    @field_validator("name")
    def validate_name(cls, value):
        if not LATTER_MATCH_PATTERN.match(value):
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                detail="Name should contains only letters")
        return value

    @field_validator("surname")
    def validate_surname(cls, value):
        if not LATTER_MATCH_PATTERN.match(value):
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                detail="Surname should contains only letters")
        return value


class DeleteUserResponse(BaseModel):
    user_id: UUID


class UpdateUserRequest(UserCreate):
    name: Optional[str] = None
    surname: Optional[str] = None
    email: Optional[EmailStr] = None
