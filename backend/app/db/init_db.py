import os
import sys
sys.path.append(os.path.abspath("../megastore-app/backend"))


from sqlalchemy.orm import Session
from app.schemas.UserCreate import UserCreate
from app.crud.repository.UserRepository import UserRepository
from app.business.abstracts.UserService import UserService

userService = UserService(UserRepository())


def init_db(db: Session) -> None:
    user = userService.getByEmail(db, email="admin@example.com")
    if not user:
        user_in = UserCreate(
            name="admindeveloper",
            fullname="admindeveloper",
            nickname="admin",
            email="superuser@example.com",
            password="superpassword",
            is_superuser=True,
        )
        user = userService.create(db, user=user_in)  # noqa: F841
