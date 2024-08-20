from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional
from pydantic.types import conint


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass


class UserResponse(BaseModel):
    name: str
    id: int
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)



class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner: UserResponse

    model_config = ConfigDict(from_attributes=True)


class PostOut(BaseModel):
    Post: PostResponse
    likes: int

    model_config = ConfigDict(from_attributes=True)


# class PostOut(BaseModel):
#     title: str
#     content: str
#     published: bool
#     id: int
#     created_at: datetime
#     owner: UserResponse
#     likes: int

#     model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str



class GroupBase(BaseModel):
    name: str
    description: str

class GroupCreate(GroupBase):
    pass

class GroupResponse(GroupBase):
    id: int
    created_at: datetime
    owner: UserResponse


    model_config = ConfigDict(from_attributes=True)

    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Like(BaseModel):
    post_id: int
    dir: conint(le=1)