import os
import sys
sys.path.append(os.path.abspath("../megastore-app/backend"))

from app.db.Session import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

