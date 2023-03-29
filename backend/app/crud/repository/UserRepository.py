import os
import sys
sys.path.append(os.path.abspath("../megastore-app/backend"))

from app.schemas.UserCreate import UserCreate, UserUpdate
from app.db.base import User
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from app.db.get_db import get_db
from fastapi import Depends
from typing import Optional, List

class UserRepository:

    def save(self, db: Session, *, user: UserCreate) -> User:
        user_db = User(name=user.name, fullname=user.fullname, nickname=user.nickname, email=user.email, password=user.password, is_superuser=user.is_superuser)
        db.add(user_db)
        db.commit()
        db.refresh(user_db)
        return user_db

    def getByEmail(self, db: Session, *, email: str) -> Optional[User]:
        user = db.query(User).filter(User.email == email).first()
        return user

    def getById(self, db: Session = Depends(get_db), *, userId: int) -> Optional[User]:
        user_query = db.query(User).filter(User.id == userId).first()
        return user_query

    def getAllUsers(self, db: Session = Depends(get_db)) -> List[User]:
        users = db.query(User).all()
        return users

    def updateUser(self, db: Session = Depends(get_db), *, userId: int, user: UserUpdate) -> User:
        user_db = self.getById(db, userId=userId)
        if not user_db:
            return False
        if isinstance(user_db, dict):
            update_data = user_db
        else:
            update_data = user.dict(exclude_unset=True)
        for field in jsonable_encoder(user_db):
            if field in update_data:
                setattr(user_db, field, update_data[field])
        db.add(user_db)
        db.commit()
        db.refresh(user_db)
        return user_db
