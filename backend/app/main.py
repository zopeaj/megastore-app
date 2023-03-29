import os
import sys
print(sys.path.append(os.path.abspath("../megastore-app/backend")))




from fastapi import FastAPI
from app.api.controller.UserController import userRouter
from app.api.controller.ProductController import productRouter
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.db.Session import engine
from app.db.base import Base

Base.metadata.create_all(bind=engine)

# app = FastAPI()


# origins = [
#     'https://localhost:3000',
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )
# app.include_router(userRouter, tags=["User"], prefix="/api/v1/user")
# app.include_router(productRouter, tags=["Product"], prefix="/api/v1/product")

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=5000)
