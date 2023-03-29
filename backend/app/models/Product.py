import os
import sys
sys.path.append(os.path.abspath("../megastore-app/backend"))


from sqlalchemy import Column, String, Integer, Float, TIMESTAMP, Sequence
from sqlalchemy.sql import func
from app.db.base_class import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, Sequence('product_id_seq'), primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    createdAt = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updateAt = Column(TIMESTAMP(timezone=True), default=None, onupdate=func.now())

    def __repr__(self):
        return "<Product(name='%s', price='%s', category='%s', createdAt='%s', updateAt='%s')>" % (self.name, self.price, self.category, self.createdAt, self.updateAt)

