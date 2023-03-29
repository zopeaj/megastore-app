import os
import sys
sys.path.append(os.path.abspath("../megastore-app/backend"))


from fastapi import APIRouter, Body, Depends, status, HTTPException
from typing import List
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.repository.UserRepository import UserRepository
from app.business.abstracts.UserService import UserService
from app.db.base import User
from app.schemas.UserCreate import UserCreate, UserUpdate
from app.db.get_db import get_db

userRouter = APIRouter()
userService = UserService(UserRepository())


@userRouter.get("/getAllUsers")
def getUsers(db: Session = Depends(get_db)) -> List[User]:
    user = userService.getUsers(db)
    return user

@userRouter.post("/create")
def createUser(payload: UserCreate, db: Session = Depends(get_db)) -> User:
    user = userService.create(db, user=payload)
    return user

@userRouter.get("/{userId}")
def get_user(userId: int, db: Session = Depends(get_db)):
    user = userService.getById(db, userId=userId)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {userId} id not found")
    return user

@userRouter.put("/{userId}")
def update_user(userId: int, payload: UserUpdate, db: Session = Depends(get_db)) -> User:
    user = userService.update(db, userId=userId, user=payload)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {userId} id not found")
    return user
