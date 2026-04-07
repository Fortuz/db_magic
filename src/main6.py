from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import DeclarativeBase, mapped_column, Session

engine = create_engine("sqlite:///db/mydatabase6.db")

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

data = {
    "name": "Alice",
    "age": "25"
}

user_input = UserCreate(**data)

session = Session(engine)

new_user = UserDB(
    name=user_input.name,
    age=user_input.age
)

session.add(new_user)
session.commit()
session.refresh(new_user)

response = UserResponse(
    id=new_user.id,
    name=new_user.name,
    age=new_user.age
)

print(response.model_dump())