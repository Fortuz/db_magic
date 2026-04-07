from fastapi import FastAPI
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import DeclarativeBase, mapped_column, Session

app = FastAPI()

engine = create_engine("sqlite:///db/mydatabase7.db")

class Base(DeclarativeBase):
    pass

class UserDB(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    age = mapped_column(Integer)

Base.metadata.create_all(engine)

class UserCreate(BaseModel):
    name: str
    age: int = Field(gt=0, lt=120)

class UserResponse(BaseModel):
    id: int
    name: str
    age: int

@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    session = Session(engine)

    new_user = UserDB(name=user.name, age=user.age)

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user

@app.get("/users", response_model=list[UserResponse])
def get_users():
    session = Session(engine)
    return session.query(UserDB).all()

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    session = Session(engine)

    user = session.query(UserDB).filter(UserDB.id == user_id).first()

    return user