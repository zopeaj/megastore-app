from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    name: Optional[str] = None
    fullname: Optional[str] = None
    nickname: Optional[str] = None
    email: EmailStr
    password: str

# Properties to receive via API on creation
class UserCreate(UserBase):
    name: str
    fullname: str
    nickname: str
    email: EmailStr
    password: str
    is_superuser: bool



class UserEmailInDBBase(UserBase):
  email: EmailStr

  class Config:
    orm_mode = True


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None
    nickname: str
    email: EmailStr



class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
