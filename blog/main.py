from fastapi import FastAPI

from . import models

from .database import engine
from .routers import blog, User,authenticate



app =FastAPI()


models.Base.metadata.create_all(bind=engine)

app.include_router(authenticate.router)
app.include_router(blog.router)
app.include_router(User.router)


         

