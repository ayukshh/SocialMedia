from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserOut(BaseModel):
        id: int
        username: str
        password: str

class config:
            orm_model=True

class UserLogin(BaseModel):
                username: str
                password: str
    