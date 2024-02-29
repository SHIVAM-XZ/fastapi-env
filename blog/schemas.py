from typing import List,Optional
from pydantic import BaseModel



class Blog(BaseModel):
    title: str
    body: str



class user(BaseModel):
    name: str
    email: str
    password: str

class showuser(BaseModel):
    name: str
    email: str

class getuser(showuser):
    blogs: List[Blog]
    class Config():
        orm_mode = True

class Show(BaseModel):
    title: str
    body: str
    creator: showuser
    
    class Config():
        orm_mode = True

class Login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
    