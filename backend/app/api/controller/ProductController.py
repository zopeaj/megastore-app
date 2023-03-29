import os
import sys
sys.path.append(os.path.abspath("../megastore-app/backend"))


from fastapi import APIRouter, Body, Depends, status, HTTPException
from typing import List
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


from app.crud.repository.UserRepository import UserRepository
from app.business.abstracts.UserService import UserService
from app.db.base import Product
from app.schemas.UserCreate import UserCreate, UserUpdate
from app.db.get_db import get_db

productRouter = APIRouter()
# productService = UserService(UserRepository())


@productRouter.get("/getAllUsers")
def getUsers():
    # user = userService.getUsers(db)
    # return user
    pass

@productRouter.post("/create")
def createUser():
    # user = userService.create(db, user=payload)
    # return user
    pass

@productRouter.get("/{userId}")
def get_user():
    # user = userService.getById(db, userId=userId)
    # if not user:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {userId} id not found")
    # return user
    pass

@productRouter.put("/{userId}")
def update_user():
    # user = userService.update(db, userId=userId, user=payload)
    # if not user:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {userId} id not found")
    # return user
    pass
