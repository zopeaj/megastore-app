import os
import sys
sys.path.append(os.path.abspath("../megastore-app/backend"))


from sqlalchemy import Integer, Column, String, Boolean, Sequence
from app.db.base_class import Base
from sqlalchemy.orm import relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Order import Order  # noqa: F401


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    fullname = Column(String, nullable=False)
    nickname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_superuser = Column(Boolean, nullable=False)
    orders = relationship("Order", back_populates="user")

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)
