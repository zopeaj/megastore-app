import os
import sys
sys.path.append(os.path.abspath("../megastore-app/backend"))


from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base_class import Base
from sqlalchemy.orm import relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .User import User  # noqa: F401


class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="orders")

    def __repr__(self):
        return "<Order(user_id='%s', user='%s')>" % (self.user_id, self.user)

