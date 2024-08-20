from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, info, auth, group, like

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# models.Base.metadata.create_all(bind=engine)
# This is for create database before using alembic


app.include_router(post.router)
app.include_router(user.router)
app.include_router(info.router)
app.include_router(auth.router)
app.include_router(group.router)
app.include_router(like.router)



@app.get('/')
def home():
    return {'message': 'Hello world'}




