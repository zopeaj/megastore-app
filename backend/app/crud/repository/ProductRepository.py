import os
import sys
sys.path.append(os.path.abspath("../megastore-app/backend"))

# from app.schemas.UserCreate import UserCreate, UserUpdate
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from app.db.get_db import get_db
from fastapi import Depends
from typing import Optional, List
from app.db.base import Product

class UserRepository:

    def save(self, ) -> User:
        # user_db = User(name=user.name, fullname=user.fullname, nickname=user.nickname, email=user.email, password=user.password, is_superuser=user.is_superuser)
        # db.add(user_db)
        # db.commit()
        # db.refresh(user_db)
        # return user_db
        pass

    def getByEmail(self):
        # user = db.query(User).filter(User.email == email).first()
        # return user
        pass

    def getById(self):
        # user_query = db.query(User).filter(User.id == userId).first()
        # return user_query
        pass

    def getAllUsers(self):
        # users = db.query(User).all()
        # return users
        pass

    def updateUser(self):
        # user_db = self.getById(db, userId=userId)
        # if not user_db:
        #     return False
        # if isinstance(user_db, dict):
        #     update_data = user_db
        # else:
        #     update_data = user.dict(exclude_unset=True)
        # for field in jsonable_encoder(user_db):
        #     if field in update_data:
        #         setattr(user_db, field, update_data[field])
        # db.add(user_db)
        # db.commit()
        # db.refresh(user_db)
        # return user_db
        pass
